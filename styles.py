"""
Stylesheet definitions for the Glass Task Manager application.
Centralizes all QSS styling for easier maintenance and customization.
iOS-style glassmorphism with refined blur and transparency.
"""

class Styles:
    """Container for all application stylesheets."""
    
    # Task Item Stylesheet
    TASK_ITEM = """
        #taskItem {
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.18);
            background-color: rgba(255, 255, 255, 0.08);
            padding: 8px;
            margin: 2px;
        }
    """
    
    # Task Item Hover Stylesheet - iOS Glassy Effect
    TASK_ITEM_HOVER = """
        #taskItem {
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.25);
            background-color: rgba(255, 255, 255, 0.15);
            padding: 8px;
            margin: 2px;
        }
    """
    
    # Checkbox Stylesheet
    CHECKBOX = """
        QCheckBox {
            color: rgba(255, 255, 255, 0.95);
            background-color: transparent;
            spacing: 8px;
            font-size: 13px;
        }
        
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 6px;
            background-color: rgba(255, 255, 255, 0.12);
            border: 1.5px solid rgba(255, 255, 255, 0.3);
        }
        
        QCheckBox::indicator:checked {
            background-color: rgba(52, 199, 89, 0.85);
            border: 1.5px solid rgba(52, 199, 89, 1);
        }
    """
    
    # Checkbox Hover Stylesheet - Enhanced visibility
    CHECKBOX_HOVER = """
        QCheckBox {
            color: rgba(255, 255, 255, 0.95);
            background-color: transparent;
            spacing: 8px;
            font-size: 13px;
        }
        
        QCheckBox::indicator {
            width: 20px;
            height: 20px;
            border-radius: 6px;
            background-color: rgba(255, 255, 255, 0.18);
            border: 1.5px solid rgba(255, 255, 255, 0.4);
        }
        
        QCheckBox::indicator:checked {
            background-color: rgba(52, 199, 89, 1);
            border: 1.5px solid rgba(52, 199, 89, 1);
        }
        
    """
    ITEM_LABEL = """
        QLabel {
            color: rgba(255, 255, 255, 0.95);
            background-color: transparent;
            font-size: 13px;
            spacing: 8px;
        }
    """

    # Delete Button Stylesheet
    DELETE_BUTTON = """
        QPushButton {
            background-color: transparent;
            color: rgba(255, 255, 255, 0.4);
            border: none;
            font-weight: normal;
            font-size: 18px;
            min-width: 26px;
            max-width: 26px;
            min-height: 26px;
            max-height: 26px;
            padding: 0px;
            margin: 0px;
            border-radius: 13px;
        }
        
        QPushButton:hover {
            background-color: none;
            color: rgba(255, 255, 255, 0.95);
            border-radius: 13px;
        }
    """
    
    # Icon Label Stylesheet
    ICON_LABEL = """
        QLabel {
            font-size: 32px;
            color: rgba(255, 255, 255, 0.95);
            background-color: transparent;
        }
    """
    
    # Title Label Stylesheet
    TITLE_LABEL = """
        QLabel {
            color: rgba(255, 255, 255, 0.95);
            font-size: 20px;
            font-weight: 600;
            padding: 8px;
            padding-bottom: 12px;
            padding-left: 12px;
            background-color: transparent;
            border: none;
            margin-bottom: 4px;
        }
    """
    
    # Scroll Area Stylesheet
    SCROLL_AREA = """
        QScrollArea {
            border: none;
            background-color: transparent;
        }
        
        QScrollBar:vertical {
            border: none;
            background: rgba(255, 255, 255, 0.05);
            width: 8px;
            border-radius: 4px;
            margin: 2px;
        }
        
        QScrollBar::handle:vertical {
            background: rgba(255, 255, 255, 0.25);
            border-radius: 4px;
            min-height: 20px;
        }
        
        QScrollBar::handle:vertical:hover {
            background: rgba(255, 255, 255, 0.35);
        }
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
            height: 0px;
        }
    """
    
    # Input Container Stylesheet
    INPUT_CONTAINER = """
        QWidget {
            background-color: transparent;
            border: none;
            padding-top: 8px;
        }
    """
    
    # Task Input Field Stylesheet
    TASK_INPUT = """
        QLineEdit {
            background-color: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.18);
            border-radius: 10px;
            padding: 8px 12px;
            color: rgba(255, 255, 255, 0.95);
            font-size: 13px;
            selection-background-color: rgba(52, 199, 89, 0.4);
        }
        
        QLineEdit:focus {
            border: 1px solid rgba(52, 199, 89, 0.6);
            background-color: rgba(255, 255, 255, 0.18);
        }
    """
    

    ADD_BUTTON = """
        QPushButton {
            background-color: rgba(52, 199, 89, 0.9);
            color: white;
            border: none;
            border-radius: 18px;
            font-size: 24px;
            font-weight: 400;
            min-width: 36px;
            max-width: 36px;
            min-height: 36px;
            max-height: 36px;
            padding: 0px;
            margin: 0px;
        }
        
        QPushButton:hover {
            background-color: rgba(52, 199, 89, 1);
        }
        
        QPushButton:pressed {
            background-color: rgba(40, 180, 70, 1);s
        }
    """

    
    # Transparent Background
    TRANSPARENT = "background-color: transparent;"
    
    @classmethod
    def get_combined_task_item(cls):
        """Returns combined stylesheet for task item (normal state)."""
        return cls.TASK_ITEM + cls.CHECKBOX + cls.ITEM_LABEL
    
    @classmethod
    def get_combined_task_item_hover(cls):
        """Returns combined stylesheet for task item (hover state)."""
        return cls.TASK_ITEM_HOVER + cls.CHECKBOX_HOVER + cls.ITEM_LABEL
