"""
Stylesheet definitions for the Glass Task Manager application.
Centralizes all QSS styling for easier maintenance and customization.
"""

class Styles:
    """Container for all application stylesheets."""
    
    # Task Item Stylesheet
    TASK_ITEM = """
        #taskItem {
            border-radius: none;
            border-left: none;
            border-right: none;
            border-top: none;
            border-bottom: 2px solid rgba(122, 200, 122, 0.3);
            background-color: transparent;
            padding: 5px;
        }
    """
    
    # Task Item Hover Stylesheet - Glassy Effect
    TASK_ITEM_HOVER = """
        #taskItem {
            border-radius: none;
            border-left: none;
            border-right: none;
            border-top: none;
            border-bottom: 2px solid rgba(144, 238, 144, 0.8);
            background-color: rgba(255, 255, 255, 0.15);
            padding: 5px;
        }
    """
    
    # Checkbox Stylesheet
    CHECKBOX = """
        QCheckBox {
            color: #ffffff;
            background-color: transparent;
            spacing: 8px;
        }
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 4px;
            background-color: rgba(255, 255, 255, 0.2);
            border: 2px solid rgba(144, 238, 144, 0.8);
        }
        QCheckBox::indicator:checked {
            background-color: rgba(46, 204, 113, 0.9);
            border: 2px solid rgba(46, 204, 113, 1);
        }
    """
    
    # Checkbox Hover Stylesheet - Enhanced visibility
    CHECKBOX_HOVER = """
        QCheckBox {
            color: #ffffff;
            background-color: transparent;
            spacing: 8px;
        }
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 4px;
            background-color: rgba(255, 255, 255, 0.3);
            border: 2px solid rgba(144, 238, 144, 1);
        }
        QCheckBox::indicator:checked {
            background-color: rgba(46, 204, 113, 1);
            border: 2px solid rgba(46, 204, 113, 1);
        }
        QCheckBox::indicator:hover {
            background-color: rgba(255, 255, 255, 0.4);
            border: 2px solid rgba(200, 255, 200, 1);
        }
    """
    
    # Delete Button Stylesheet
    DELETE_BUTTON = """
        QPushButton {
            background-color: transparent;
            color: rgba(200, 200, 200, 0.5);
            border: none;
            font-weight: bold;
            font-size: 20px;
            min-width: 24px;
            max-width: 24px;
            min-height: 24px;
            max-height: 24px;
            padding: 0px;
            margin: 0px;
        }
        QPushButton:hover {
            background-color: rgba(255, 100, 100, 0.3);
            color: rgba(255, 255, 255, 1);
            border-radius: 12px;
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
            color: #ffffff;
            font-size: 19px;
            font-weight: bold;
            padding: 1px;
            padding-bottom: 5px;
            padding-top: 5px;
            padding-left: 10px;
            background-color: none;
            border-left: none;
            border-right: none;
            border-top: none;
            border-bottom: 2px solid rgba(144, 238, 144, 0.4);
            border-radius: none;
            margin-bottom: 10px;
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
            background: rgba(255, 255, 255, 0.08);
            width: 10px;
            border-radius: 5px;
            margin: 2px;
        }
        QScrollBar::handle:vertical {
            background: rgba(46, 204, 113, 0.5);
            border-radius: 5px;
            min-height: 20px;
        }
        QScrollBar::handle:vertical:hover {
            background: rgba(46, 204, 113, 0.7);
        }
    """
    
    # Input Container Stylesheet
    INPUT_CONTAINER = """
        QWidget {

            border-radius: none;
            border-left: none;
            border-right: none;
            border-bottom: none;
            border-top: 3px solid rgba(46, 204, 113, 0.4);


        }
    """
    
    # Task Input Field Stylesheet
    TASK_INPUT = """
        QLineEdit {
            background-color: rgba(255, 255, 255, 0.15);
            border: 2px solid rgba(46, 204, 113, 0.4);
            border-radius: none;
            border-left: none;
            border-right: none;
            border-top: none;
            border-bottom: 2px solid rgba(144, 238, 144, 0.5);
            padding: 5px;
            color: #ffffff;
            font-size: 13px;
            outline: none;
        }
        QLineEdit:focus {
            border: 2px solid rgba(46, 204, 113, 0.8);
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: none;
            border-left: none;
            border-right: none;
            border-top: none;
            border-bottom: 2px solid rgba(144, 238, 144, 0.5);
            outline: none;
        }
    """
    
    # Add Button Stylesheet
    ADD_BUTTON = """
        QPushButton {
            background-color: none;
            color: white;
            border: none;
            border-radius: none;
            font-size: 24px;
            min-width: 20px;
            max-width: 20px;
            min-height: 20px;
            max-height: 20px;
        }
        QPushButton:hover {
            background-color: rgba(39, 174, 96, 0.9);
            border-radius: 10px;
        }
    """
    
    # Transparent Background
    TRANSPARENT = "background-color: transparent;"
    
    @classmethod
    def get_combined_task_item(cls):
        """Returns combined stylesheet for task item (normal state)."""
        return cls.TASK_ITEM + cls.CHECKBOX
    
    @classmethod
    def get_combined_task_item_hover(cls):
        """Returns combined stylesheet for task item (hover state)."""
        return cls.TASK_ITEM_HOVER + cls.CHECKBOX_HOVER
