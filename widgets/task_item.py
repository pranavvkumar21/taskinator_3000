"""
TaskItem widget - Represents a single task in the task list.
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QLabel,
                             QCheckBox, QGraphicsDropShadowEffect, QSizePolicy)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QLinearGradient, QPen
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles import Styles

class TaskItem(QWidget):
    """
    A custom widget representing a single task item with checkbox and delete button.
    Features glassy hover effect.
    
    Args:
        text (str): The task description text
        parent (QWidget, optional): Parent widget
    """
    
    state_changed = pyqtSignal()
    
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.is_hovering = False
        self.hover_opacity = 0  # For smooth transitions
        
        # Setup widget
        self._setup_widget()
        
        # Create UI elements
        self._setup_ui(text)
        
        # Apply styles
        self._apply_styles()
    
    def _setup_widget(self):
        """Configure widget properties."""
        # Enable background painting
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName("taskItem")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    
    def _setup_ui(self, text):
        """Create and configure UI elements."""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(1, 1, 1, 1)
        
        # Checkbox
        self.checkbox = QCheckBox()
        self.checkbox.setFocusPolicy(Qt.NoFocus)  # Prevent focus highlight
        
        # Connect checkbox state change to emit signal
        self.checkbox.stateChanged.connect(self.state_changed.emit)

        self.label = QLabel(text)
        self.label.setWordWrap(True)
        self.label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        
        # Delete button
        self.delete_btn = self._create_delete_button()
        
        # Add widgets to layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label,stretch=1)
        layout.addStretch()  # Push delete button to the right
        layout.addWidget(self.delete_btn)
    
    def _create_delete_button(self):
        """
        Create and configure the delete button.
        
        Returns:
            QPushButton: Configured delete button
        """
        btn = QPushButton("×")
        btn.setFocusPolicy(Qt.NoFocus)
        return btn
    
    def _apply_styles(self):
        """Apply stylesheets to widgets."""
        self.setStyleSheet(Styles.get_combined_task_item())
        self.delete_btn.setStyleSheet(Styles.DELETE_BUTTON)
    
    def enterEvent(self, event):
        """Handle mouse enter - apply glassy hover effect."""
        self.is_hovering = True
        self.setStyleSheet(Styles.get_combined_task_item_hover())
        self.update()  # Trigger repaint for glass effect
        super().enterEvent(event)
    
    def leaveEvent(self, event):
        """Handle mouse leave - remove hover effect."""
        self.is_hovering = False
        self.setStyleSheet(Styles.get_combined_task_item())
        self.update()
        super().leaveEvent(event)
    
    def paintEvent(self, event):
        """Paint with enhanced glass effect on hover."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        if self.is_hovering:
            # Enhanced glass effect on hover
            path = QPainterPath()
            path.addRoundedRect(2, 2, self.width()-4, self.height()-4, 8, 8)
            
            # Glassy shine overlay
            shine_gradient = QLinearGradient(0, 0, 0, self.height())
            shine_gradient.setColorAt(0, QColor(255, 255, 255, 45))
            shine_gradient.setColorAt(0.5, QColor(255, 255, 255, 25))
            shine_gradient.setColorAt(1, QColor(255, 255, 255, 5))
            painter.fillPath(path, shine_gradient)
            
            # Glow border
            pen = QPen(QColor(255, 255, 255, 80))
            pen.setWidth(2)
            painter.setPen(pen)
            painter.drawPath(path)
        
        super().paintEvent(event)
    
    def get_text(self):
        """Get the task text."""
        return self.label.text()
    
    def is_completed(self):
        """Check if task is completed."""
        return self.checkbox.isChecked()
    
    def set_completed(self, completed):
        """Set task completion state."""
        self.checkbox.setChecked(completed)
