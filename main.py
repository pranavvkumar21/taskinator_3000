"""
Glass Task Manager - Main application entry point.

A beautiful task management application with glass morphism design.
Features expandable/collapsible interface with smooth animations.
"""

import sys
from PyQt5.QtWidgets import QApplication
from widgets import GlassTaskList


def main():
    """Initialize and run the application."""
    app = QApplication(sys.argv)
    
    # Set application metadata
    app.setApplicationName("Glass Task Manager")
    app.setOrganizationName("GlassApps")
    
    # Create and show main widget
    widget = GlassTaskList()
    widget.show()
    
    # Start event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
