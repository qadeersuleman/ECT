import sys
import qtawesome as qta
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QStackedWidget,
    QFrame
)

from sidebar import SidebarWidget
from dashboard_page import DashboardPage
from bill_management_page import BillManagementPage
from styles import MAIN_STYLE

class GenericPageWidget(QWidget):
    """Placeholder Widget for other pages (Budget Management, Expenditure, etc.)"""
    def __init__(self, page_name: str, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        layout.setContentsMargins(24, 24, 24, 24)
        layout.setSpacing(16)

        header_lbl = QLabel(page_name)
        header_lbl.setStyleSheet("color: #0F172A; font-size: 22px; font-weight: bold;")
        layout.addWidget(header_lbl)

        card = QFrame()
        card.setStyleSheet("background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 10px;")
        card_layout = QVBoxLayout(card)
        card_layout.setContentsMargins(24, 24, 24, 24)

        t_lbl = QLabel(f"{page_name} Workspace")
        t_lbl.setStyleSheet("color: #0F172A; font-size: 16px; font-weight: bold;")

        desc_lbl = QLabel(
            f"This is the dedicated workspace container for '{page_name}'. "
            "You can easily add tables, forms, and business logic here."
        )
        desc_lbl.setStyleSheet("color: #64748B; font-size: 13.5px;")

        card_layout.addWidget(t_lbl)
        card_layout.addWidget(desc_lbl)
        card_layout.addStretch()

        layout.addWidget(card, 1)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EC - Budget & Bills Management System")
        self.resize(1380, 840)
        self.setMinimumSize(1080, 700)

        # Set Window Icon
        app_icon = qta.icon("fa5s.shield-alt", color="#38BDF8")
        self.setWindowIcon(app_icon)

        # Main Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        root_layout = QHBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # 1. Left Dark Navy Sidebar
        self.sidebar = SidebarWidget()
        self.sidebar.item_selected.connect(self.on_nav_selected)
        root_layout.addWidget(self.sidebar)

        # 2. Right Main Executive Content Area
        main_content = QWidget()
        main_content.setObjectName("MainContentArea")
        content_layout = QVBoxLayout(main_content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Stacked Pages
        self.stacked_widget = QStackedWidget()

        # Index 0: Dashboard Page (100% exact replica of screenshot)
        self.dashboard_page = DashboardPage()
        self.stacked_widget.addWidget(self.dashboard_page)

        # Index 1: Bill Management Page (Create Contingent Bill - 100% exact replica of screenshot)
        self.bill_management_page = BillManagementPage()
        self.stacked_widget.addWidget(self.bill_management_page)

        # Other Pages (Index 2 to 10)
        other_pages = [
            "Budget Management",
            "Expenditure",
            "Vendors",
            "Reports",
            "Tax Management",
            "Settings",
            "Users",
            "Backup & Restore",
            "Logout"
        ]

        for p_name in other_pages:
            self.stacked_widget.addWidget(GenericPageWidget(p_name))

        content_layout.addWidget(self.stacked_widget, 1)
        root_layout.addWidget(main_content, 1)

    def on_nav_selected(self, index: int, title: str):
        self.stacked_widget.setCurrentIndex(index)


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(MAIN_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
