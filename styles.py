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
            border-radius: 10px;
            background-color: #f0f0f0;
            padding: 8px;
            margin: 3px;
            border: none;
        }
    """
    
    # Task Item Hover Stylesheet - Neumorphic raised effect
    TASK_ITEM_HOVER = """
        #taskItem {
            border-radius: 10px;
            background-color: #efefef;
            padding: 8px;
            margin: 3px;
            border: none;
        }
    """
    
    # Checkbox Stylesheet
    CHECKBOX = """
        QCheckBox {
            color: #444444;
            background-color: transparent;
            spacing: 8px;
            font-size: 13px;
        }
        
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 5px;
            background-color: #f0f0f0;
            border: 1px solid #d0d0d0;
        }
        
        QCheckBox::indicator:checked {
            background-color: #68b99a;
            border: 1px solid #5aaa8a;
        }
    """
    
    # Checkbox Hover Stylesheet
    CHECKBOX_HOVER = """
        QCheckBox {
            color: #333333;
            background-color: transparent;
            spacing: 8px;
            font-size: 13px;
        }
        
        QCheckBox::indicator {
            width: 18px;
            height: 18px;
            border-radius: 5px;
            background-color: #e8e8e8;
            border: 1px solid #c0c0c0;
        }
        
        QCheckBox::indicator:checked {
            background-color: #5aaa8a;
            border: 1px solid #4a9a7a;
        }
        
    """
    ITEM_LABEL = """
        QLabel {
            color: #444444;
            background-color: transparent;
            font-size: 13px;
        }
    """

    # Delete Button Stylesheet
    DELETE_BUTTON = """
        QPushButton {
            background-color: transparent;
            color: #bbbbbb;
            border: none;
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
            background-color: #e0e0e0;
            color: #cc5555;
            border-radius: 13px;
        }
    """
    
    # Icon Label Stylesheet
    ICON_LABEL = """
        QLabel {
            font-size: 32px;
            color: #444444;
            background-color: transparent;
        }
    """
    
    # Title Label Stylesheet
    TITLE_LABEL = """
        QLabel {
            color: #333333;
            font-size: 18px;
            font-weight: 600;
            padding: 8px;
            padding-left: 12px;
            background-color: transparent;
            border: none;
        }
    """

    # Close Button Stylesheet
    CLOSE_BUTTON = """
        QPushButton {
            background-color: transparent;
            color: #aaaaaa;
            border: none;
            font-size: 14px;
            min-width: 24px;
            max-width: 24px;
            min-height: 24px;
            max-height: 24px;
            padding: 0px;
            border-radius: 12px;
        }
        QPushButton:hover {
            background-color: #e0e0e0;
            color: #cc5555;
        }
        QPushButton:pressed {
            background-color: #d8d8d8;
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
            background: #e8e8e8;
            width: 6px;
            border-radius: 3px;
            margin: 2px;
        }
        
        QScrollBar::handle:vertical {
            background: #c8c8c8;
            border-radius: 3px;
            min-height: 20px;
        }
        
        QScrollBar::handle:vertical:hover {
            background: #aaaaaa;
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
            background-color: #f0f0f0;
            border: none;
            border-radius: 10px;
            padding: 8px 12px;
            color: #444444;
            font-size: 13px;
            selection-background-color: rgba(104, 185, 154, 0.4);
        }
        
        QLineEdit:focus {
            border: 1px solid #d0d0d0;
            background-color: #f5f5f5;
        }
    """
    

    ADD_BUTTON = """
        QPushButton {
            background-color: #f0f0f0;
            color: #68b99a;
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
            background-color: #e8e8e8;
            color: #5aaa8a;
        }
        
        QPushButton:pressed {
            background-color: #e0e0e0;
            color: #4a9a7a;
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
