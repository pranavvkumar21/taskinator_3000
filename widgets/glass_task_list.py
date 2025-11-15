"""
GlassTaskList widget - Main application window with glass morphism effect.
"""

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLineEdit, QScrollArea, QLabel,
                             QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QSize
from PyQt5.QtGui import (QPainter, QColor, QPainterPath, QLinearGradient, 
                         QRadialGradient, QPen)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QPoint, QSize, QParallelAnimationGroup
from PyQt5.QtGui import QPixmap

import sys
import json
import os
from pathlib import Path


# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import Styles
from widgets.task_item import TaskItem


class GlassTaskList(QWidget):
    """
    Main application widget with glass morphism design.
    Features expandable/collapsible interface with task management.
    """
    
    def __init__(self):
        super().__init__()
        self.dragging = False
        self.drag_start_pos = None
        self.offset = QPoint()
        self.expanded = False
        self.task_items = []
        self.animation_progress = 0.0 
        # Size configurations
        self.collapsed_size = QSize(70, 70)
        self.expanded_size = QSize(300, 420)
        
        self._setup_window()
        self._setup_ui()
        self._setup_animation()
        self._setup_effects()
        self._position_window()
        self.load_tasks()
    def _setup_window(self):
        """Configure window properties."""
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.resize(self.collapsed_size)
        
    def _setup_ui(self):
        """Create and configure UI elements."""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(7, 15, 7, 15)
        
        # Icon label (collapsed state)
        self.icon_label = self._create_icon_label()
        main_layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        
        # Task list container (expanded state)
        self.list_container = self._create_list_container()
        main_layout.addWidget(self.list_container)
        
    def _create_icon_label(self):
        """Create the icon label for collapsed state."""
        label = QLabel()
        label.setAlignment(Qt.AlignCenter)
        
        # Load image icon
        pixmap = QPixmap("icon.png")  # Replace with your image path
        
        # Scale the image to fit the collapsed size (with some padding)
        scaled_pixmap = pixmap.scaled(
            40, 40,  # Icon size (adjust as needed)
            Qt.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )
        
        label.setPixmap(scaled_pixmap)
        label.setStyleSheet("background-color: transparent;")
        
        return label

        
    def _create_list_container(self):
        """Create the main list container for expanded state."""
        container = QWidget()
        container.setStyleSheet(Styles.TRANSPARENT)
        container.hide()
        
        list_layout = QVBoxLayout(container)
        list_layout.setContentsMargins(0, 0, 0, 0)
        list_layout.setSpacing(8)
        
        # Title
        title = QLabel("Task List")
        title.setStyleSheet(Styles.TITLE_LABEL)
        title.setAlignment(Qt.AlignLeft)
        list_layout.addWidget(title)
        
        # Scroll area
        scroll = self._create_scroll_area()
        list_layout.addWidget(scroll)
        
        # Input container
        input_container = self._create_input_container()
        list_layout.addWidget(input_container)
        
        return container
        
    def _create_scroll_area(self):
        """Create the scrollable task area."""
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet(Styles.SCROLL_AREA)
        
        self.task_widget = QWidget()
        self.task_widget.setStyleSheet(Styles.TRANSPARENT)
        self.task_layout = QVBoxLayout(self.task_widget)
        self.task_layout.setAlignment(Qt.AlignTop)
        self.task_layout.setSpacing(3)
        self.task_layout.setContentsMargins(2, 2, 2, 2)
        
        scroll.setWidget(self.task_widget)
        return scroll
        
    def _create_input_container(self):
        """Create the input field and add button container."""
        container = QWidget()
        container.setStyleSheet(Styles.INPUT_CONTAINER)
        
        input_layout = QHBoxLayout(container)
        input_layout.setSpacing(8)
        
        # Task input field
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Add new task...")
        self.task_input.setStyleSheet(Styles.TASK_INPUT)
        self.task_input.returnPressed.connect(self.add_task)
        
        # Add button
        add_btn = QPushButton("+")
        add_btn.setStyleSheet(Styles.ADD_BUTTON)
        add_btn.clicked.connect(self.add_task)
        
        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_btn)
        
        return container
        
        
    def _setup_effects(self):
        """Setup visual effects like drop shadow."""
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setColor(QColor(0, 0, 0, 160))
        shadow.setOffset(0, 8)
        self.setGraphicsEffect(shadow)
        
    def _position_window(self):
        """Position window in bottom-right corner of screen."""
        screen = QApplication.primaryScreen().geometry()
        self.move(screen.width() - 120, screen.height() - 120)
            
    def _get_data_file_path(self):
        """Get the path to the tasks data file."""
        # Save in data folder in parent directory
        home = Path(__file__).parent.parent
        app_data_dir = home / "data"
        
        # Create directory if it doesn't exist
        app_data_dir.mkdir(exist_ok=True)
        
        return app_data_dir / "tasks.json"

    def save_tasks(self):
        """Save all tasks and their checked states to a JSON file."""
        tasks_data = []
        
        for task_item in self.task_items:
            task_data = {
                "text": task_item.checkbox.text(),
                "checked": task_item.checkbox.isChecked()
            }
            tasks_data.append(task_data)
        
        # Save to file
        try:
            file_path = self._get_data_file_path()
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(tasks_data, f, indent=2, ensure_ascii=False)
            print(f"Tasks saved to {file_path}")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def load_tasks(self):
        """Load tasks and their checked states from JSON file."""
        file_path = self._get_data_file_path()
        
        # Check if file exists
        if not file_path.exists():
            print("No saved tasks found.")
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tasks_data = json.load(f)
            
            # Clear existing tasks
            for task_item in self.task_items[:]:
                self.remove_task(task_item)
            
            # Load saved tasks
            for task_data in tasks_data:
                task = TaskItem(task_data["text"])
                task.checkbox.setChecked(task_data["checked"])
                task.delete_btn.clicked.connect(lambda checked, t=task: self.remove_task(t))
                task.state_changed.connect(self.save_tasks)
                self.task_layout.addWidget(task)
                self.task_items.append(task)
            
            print(f"Loaded {len(tasks_data)} tasks from {file_path}")
        except Exception as e:
            print(f"Error loading tasks: {e}")

    def add_task(self):
        """Add a new task to the list."""
        text = self.task_input.text().strip()
        if text:
            task = TaskItem(text)
            task.delete_btn.clicked.connect(lambda: self.remove_task(task))
            task.state_changed.connect(self.save_tasks)
            self.task_layout.addWidget(task)
            self.task_items.append(task)
            self.task_input.clear()
            
            # Auto-save after adding task
            self.save_tasks()

    def remove_task(self, task):
        """
        Remove a task from the list.
        
        Args:
            task (TaskItem): The task widget to remove
        """
        self.task_layout.removeWidget(task)
        self.task_items.remove(task)
        task.deleteLater()
        
        # Auto-save after removing task
        self.save_tasks()

        
    def paintEvent(self, event):
        """
        Custom paint event for glass morphism effect.
        Creates multi-layer 3D glass appearance.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Create path
        path = QPainterPath()
        if self.animation_progress < 0.2:
            # Draw circle when mostly collapsed
            path.addEllipse(5, 5, self.width()-10, self.height()-10)
        else:
            # Draw rounded rectangle when expanding/expanded
            path.addRoundedRect(5, 5, self.width()-10, self.height()-10, 25, 25)

            
        # Layer 1: Base dark layer for depth
        self._paint_base_layer(painter, path)
        
        # Layer 2: Glass gradient overlay
        self._paint_glass_layer(painter, path)
        
        # Layer 3: Radial highlight
        self._paint_radial_highlight(painter, path)
        
        # Borders
        self._paint_borders(painter, path)
        
        # Bottom reflection
        if self.expanded:
            self._paint_bottom_reflection(painter)
            
    def _paint_base_layer(self, painter, path):
        """Paint the base dark layer."""
        base_gradient = QLinearGradient(0, 0, 0, self.height())
        base_gradient.setColorAt(0, QColor(25, 120, 65, 140))
        base_gradient.setColorAt(0.5, QColor(34, 139, 75, 150))
        base_gradient.setColorAt(1, QColor(20, 100, 55, 140))
        painter.fillPath(path, base_gradient)
        
    def _paint_glass_layer(self, painter, path):
        """Paint the glass gradient overlay."""
        glass_gradient = QLinearGradient(0, 0, 0, self.height())
        glass_gradient.setColorAt(0, QColor(255, 255, 255, 60))
        glass_gradient.setColorAt(0.3, QColor(255, 255, 255, 20))
        glass_gradient.setColorAt(0.7, QColor(0, 0, 0, 15))
        glass_gradient.setColorAt(1, QColor(0, 0, 0, 40))
        painter.fillPath(path, glass_gradient)
        
    def _paint_radial_highlight(self, painter, path):
        """Paint the radial glossy highlight."""
        if not self.expanded:
            center_x = self.width() // 2
            center_y = self.height() // 3
        else:
            center_x = self.width() // 2
            center_y = 40
            
        radial = QRadialGradient(center_x, center_y, self.width() * 0.6)
        radial.setColorAt(0, QColor(255, 255, 255, 80))
        radial.setColorAt(0.4, QColor(255, 255, 255, 30))
        radial.setColorAt(1, QColor(255, 255, 255, 0))
        painter.fillPath(path, radial)
        
    def _paint_borders(self, painter, path):
        """Paint outer and inner borders."""
        # Outer border
        pen = QPen()
        pen.setWidth(2)
        border_gradient = QLinearGradient(0, 0, 0, self.height())
        border_gradient.setColorAt(0, QColor(144, 238, 144, 200))
        border_gradient.setColorAt(0.5, QColor(46, 204, 113, 180))
        border_gradient.setColorAt(1, QColor(144, 238, 144, 160))
        pen.setBrush(border_gradient)
        painter.setPen(pen)
        painter.drawPath(path)
        
        # Inner highlight border
        inner_path = QPainterPath()
        if self.expanded:
            inner_path.addRoundedRect(7, 7, self.width()-14, self.height()-14, 23, 23)
        else:
            inner_path.addEllipse(7, 7, self.width()-14, self.height()-14)
            
        inner_pen = QPen()
        inner_pen.setWidth(1)
        inner_pen.setColor(QColor(200, 255, 200, 100))
        painter.setPen(inner_pen)
        painter.drawPath(inner_path)
        
    def _paint_bottom_reflection(self, painter):
        """Paint bottom reflection line for depth."""
        bottom_line_gradient = QLinearGradient(0, self.height()-20, 0, self.height()-5)
        bottom_line_gradient.setColorAt(0, QColor(255, 255, 255, 0))
        bottom_line_gradient.setColorAt(0.5, QColor(255, 255, 255, 25))
        bottom_line_gradient.setColorAt(1, QColor(255, 255, 255, 0))
        
        shine_path = QPainterPath()
        shine_path.addRoundedRect(15, self.height()-25, self.width()-30, 15, 8, 8)
        painter.fillPath(shine_path, bottom_line_gradient)

    def mousePressEvent(self, event):
        """Handle mouse press for dragging."""
        if event.button() == Qt.LeftButton:
            self.drag_start_pos = event.pos()
            self.offset = event.pos()
            
    def mouseMoveEvent(self, event):
        """Handle mouse move for dragging."""
        if event.buttons() == Qt.LeftButton and self.drag_start_pos is not None:
            if (event.pos() - self.drag_start_pos).manhattanLength() > 5:
                self.dragging = True
                self.move(self.mapToGlobal(event.pos() - self.offset))
                
    def mouseReleaseEvent(self, event):
        """Handle mouse release for toggle/drag completion."""
        if event.button() == Qt.LeftButton:
            if not self.dragging:
                if not self.expanded or event.pos().y() < 50:
                    if self.expanded:
                        self.collapse()
                    else:
                        self.expand()
                        
            self.dragging = False
            self.drag_start_pos = None
            

    def _setup_animation(self):
        """Setup expand/collapse animations for both size and position."""
        # Size animation
        self.size_anim = QPropertyAnimation(self, b"size")
        self.size_anim.setDuration(350)
        self.size_anim.setEasingCurve(QEasingCurve.InOutQuad)
        
        # Position animation
        self.pos_anim = QPropertyAnimation(self, b"pos")
        self.pos_anim.setDuration(350)
        self.pos_anim.setEasingCurve(QEasingCurve.InOutQuad)
        
        # Animation group
        from PyQt5.QtCore import QParallelAnimationGroup
        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.size_anim)
        self.anim_group.addAnimation(self.pos_anim)
        
        # Connect to track animation progress
        self.size_anim.valueChanged.connect(self._on_animation_progress)

    def _on_animation_progress(self, value):
        """Update animation progress and trigger repaint."""
        # Calculate progress based on current size
        if self.expanded:
            # Expanding: progress from 0 to 1
            width_progress = (value.width() - self.collapsed_size.width()) / \
                            (self.expanded_size.width() - self.collapsed_size.width())
            self.animation_progress = max(0.0, min(1.0, width_progress))
        else:
            # Collapsing: progress from 1 to 0
            width_progress = (value.width() - self.collapsed_size.width()) / \
                            (self.expanded_size.width() - self.collapsed_size.width())
            self.animation_progress = max(0.0, min(1.0, width_progress))
        
        self.update()  # Trigger repaint

    def expand(self):
        """Expand the widget leftward and downward, with top-right anchored."""
        # Set expanded flag first
        self.expanded = True
        
        # Get current position
        current_pos = self.pos()
        current_size = self.size()
        
        # Calculate the top-right corner position
        top_right_x = current_pos.x() + current_size.width()
        top_y = current_pos.y()
        
        # Calculate target position (move left as we expand)
        target_x = top_right_x - self.expanded_size.width()
        target_y = top_y
        
        # Hide icon but DON'T show list_container yet
        self.icon_label.hide()
        # Keep list_container hidden during animation
        self.list_container.hide()
        
        # Setup animations
        self.size_anim.setStartValue(current_size)
        self.size_anim.setEndValue(self.expanded_size)
        
        self.pos_anim.setStartValue(current_pos)
        self.pos_anim.setEndValue(QPoint(target_x, target_y))
        
        # Disconnect previous connections to avoid multiple triggers
        try:
            self.anim_group.finished.disconnect()
        except:
            pass
        
        # Show list container ONLY AFTER animation completes
        self.anim_group.finished.connect(lambda: self.list_container.show())
        
        # Start both animations together
        self.anim_group.start()


    def collapse(self):
        """Collapse the widget rightward and upward, with top-right anchored."""
        # Get current position BEFORE changing expanded flag
        current_pos = self.pos()
        current_size = self.size()
        
        # Calculate the top-right corner position
        top_right_x = current_pos.x() + current_size.width()
        top_y = current_pos.y()
        
        # Calculate target position (move right as we collapse)
        target_x = top_right_x - self.collapsed_size.width()
        target_y = top_y
        
        # Hide list container and show icon IMMEDIATELY (before animation)
        self.list_container.hide()
        self.icon_label.show()
        
        # Set collapsed flag AFTER hiding content
        self.expanded = False
        
        # Setup animations
        self.size_anim.setStartValue(current_size)
        self.size_anim.setEndValue(self.collapsed_size)
        
        self.pos_anim.setStartValue(current_pos)
        self.pos_anim.setEndValue(QPoint(target_x, target_y))
        
        # Disconnect previous connections
        try:
            self.anim_group.finished.disconnect()
        except:
            pass
        
        # Start both animations together
        self.anim_group.start()

