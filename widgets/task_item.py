"""
TaskItem widget - Represents a single task in the task list.
"""

from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton, 
                             QCheckBox, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSizePolicy
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
        self._setup_widget()
        self._setup_ui(text)
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
        self.checkbox = QCheckBox(text)
        self.checkbox.setFocusPolicy(Qt.NoFocus)  # Prevent focus highlight
        
        # Connect checkbox state change to emit signal
        self.checkbox.stateChanged.connect(self.state_changed.emit)
        
        # Delete button
        self.delete_btn = self._create_delete_button()
        
        # Add widgets to layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.delete_btn)
        
    def _create_delete_button(self):
        """
        Create and configure the delete button with glow effect.
        
        Returns:
            QPushButton: Configured delete button
        """
        btn = QPushButton("×")
        btn.clicked.connect(lambda: None)  # Placeholder, will be connected in parent
        return btn
        
    def _apply_styles(self):
        """Apply stylesheets to widgets."""
        self.setStyleSheet(Styles.get_combined_task_item())
        self.delete_btn.setStyleSheet(Styles.DELETE_BUTTON)
        
    def enterEvent(self, event):
        """Handle mouse enter - apply glassy hover effect."""
        self.setStyleSheet(Styles.get_combined_task_item_hover())
        super().enterEvent(event)
        
    def leaveEvent(self, event):
        """Handle mouse leave - remove hover effect."""
        self.setStyleSheet(Styles.get_combined_task_item())
        super().leaveEvent(event)
