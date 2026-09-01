import qtawesome as qta
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFrame,
    QScrollArea
)

class SidebarWidget(QWidget):
    item_selected = pyqtSignal(int, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("SidebarContainer")
        self.setFixedWidth(275)
        self.setStyleSheet("background-color: #03162A;")
        self.nav_buttons = []
        self.current_active_index = 0

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(14, 16, 14, 16)
        main_layout.setSpacing(14)

        # ----------------------------------------------------
        # 1. Top Card: DDO Information
        # ----------------------------------------------------
        ddo_card = QFrame()
        ddo_card.setObjectName("DDOInfoCard")
        ddo_card.setStyleSheet("""
            QFrame#DDOInfoCard {
                background-color: rgba(4, 25, 48, 0.7);
                border: 1px solid rgba(255, 255, 255, 0.22);
                border-radius: 8px;
            }
        """)
        ddo_layout = QVBoxLayout(ddo_card)
        ddo_layout.setContentsMargins(12, 10, 12, 12)
        ddo_layout.setSpacing(8)

        # Title
        title_label = QLabel("DDO Information")
        title_label.setObjectName("DDOTitle")
        title_label.setStyleSheet("color: #FFFFFF; font-size: 13px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ddo_layout.addWidget(title_label)

        # 2 Columns (DDO Code | GH-0018 CENTERAL)
        info_layout = QHBoxLayout()
        info_layout.setContentsMargins(4, 4, 4, 4)
        info_layout.setSpacing(8)

        # Left Column: DDO Code
        left_box = QVBoxLayout()
        left_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ddo_code_label = QLabel("DDO Code")
        ddo_code_label.setStyleSheet("color: #FFFFFF; font-size: 13px; font-weight: 600;")
        ddo_code_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left_box.addWidget(ddo_code_label)
        info_layout.addLayout(left_box, 1)

        # Vertical Divider Line
        v_divider = QFrame()
        v_divider.setStyleSheet("background-color: rgba(255, 255, 255, 0.2); width: 1px; border: none;")
        v_divider.setFrameShape(QFrame.Shape.VLine)
        v_divider.setFrameShadow(QFrame.Shadow.Plain)
        info_layout.addWidget(v_divider)

        # Right Column: GH-0018 / CENTERAL
        right_box = QVBoxLayout()
        right_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
        right_box.setSpacing(2)
        
        ddo_val_label = QLabel("GH-0018")
        ddo_val_label.setStyleSheet("color: #FFFFFF; font-size: 16px; font-weight: bold;")
        ddo_val_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        ddo_central_label = QLabel("CENTERAL")
        ddo_central_label.setStyleSheet("color: #FFFFFF; font-size: 11px; font-weight: bold;")
        ddo_central_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        right_box.addWidget(ddo_val_label)
        right_box.addWidget(ddo_central_label)
        info_layout.addLayout(right_box, 1)

        ddo_layout.addLayout(info_layout)
        main_layout.addWidget(ddo_card)

        # ----------------------------------------------------
        # 2. Navigation Menu Items List
        # ----------------------------------------------------
        nav_scroll = QScrollArea()
        nav_scroll.setWidgetResizable(True)
        nav_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        nav_container = QWidget()
        nav_container.setStyleSheet("background: transparent;")
        nav_layout = QVBoxLayout(nav_container)
        nav_layout.setContentsMargins(0, 2, 0, 2)
        nav_layout.setSpacing(4)

        # 11 Menu Items Configuration matching original image
        items_data = [
            ("Dashboard", "fa5s.home", False),
            ("Bill Management", "fa5s.file-alt", True),  # Chevron icon >
            ("Budget Management", "fa5s.calendar-alt", False),
            ("Expenditure", "fa5s.chart-line", False),
            ("Vendors", "fa5s.store", False),
            ("Reports", "fa5s.file-contract", False),
            ("Tax Management", "fa5s.shield-alt", False),
            ("Settings", "fa5s.cog", False),
            ("Users", "fa5s.user-friends", False),
            ("Backup & Restore", "fa5s.cloud-download-alt", False),
            ("Logout", "fa5s.sign-out-alt", False),
        ]

        for index, (title, icon_name, has_chevron) in enumerate(items_data):
            btn = self.create_nav_button(index, title, icon_name, has_chevron)
            nav_layout.addWidget(btn)
            self.nav_buttons.append(btn)

        nav_layout.addStretch()
        nav_scroll.setWidget(nav_container)
        main_layout.addWidget(nav_scroll, 1)

        # Set initial active item (Dashboard)
        self.set_active_item(0)

        # ----------------------------------------------------
        # 3. Bottom Financial Year Footer
        # ----------------------------------------------------
        h_divider = QFrame()
        h_divider.setStyleSheet("background-color: rgba(255, 255, 255, 0.2); max-height: 1px; border: none;")
        h_divider.setFrameShape(QFrame.Shape.HLine)
        h_divider.setFrameShadow(QFrame.Shadow.Plain)
        main_layout.addWidget(h_divider)

        footer_layout = QHBoxLayout()
        footer_layout.setContentsMargins(4, 4, 4, 4)
        footer_layout.setSpacing(10)

        # Left Info
        fin_year_box = QVBoxLayout()
        fin_year_box.setSpacing(2)
        
        lbl_fin_title = QLabel("Financial Year")
        lbl_fin_title.setStyleSheet("color: #94A3B8; font-size: 11px; font-weight: 500;")
        
        lbl_fin_val = QLabel("2026 - 2027")
        lbl_fin_val.setStyleSheet("color: #FFFFFF; font-size: 14px; font-weight: bold;")

        fin_year_box.addWidget(lbl_fin_title)
        fin_year_box.addWidget(lbl_fin_val)
        footer_layout.addLayout(fin_year_box, 1)

        # Right Calendar Icon Box
        cal_box = QFrame()
        cal_box.setFixedSize(36, 36)
        cal_box.setStyleSheet("border: 1px solid rgba(255, 255, 255, 0.3); border-radius: 6px; background-color: transparent;")
        cal_layout = QVBoxLayout(cal_box)
        cal_layout.setContentsMargins(0, 0, 0, 0)
        cal_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cal_icon_lbl = QLabel()
        cal_icon = qta.icon("fa5s.calendar-alt", color="white")
        cal_icon_lbl.setPixmap(cal_icon.pixmap(18, 18))
        cal_icon_lbl.setStyleSheet("background: transparent; border: none;")
        cal_icon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cal_layout.addWidget(cal_icon_lbl)

        footer_layout.addWidget(cal_box)
        main_layout.addLayout(footer_layout)

    def create_nav_button(self, index: int, title: str, icon_name: str, has_chevron: bool) -> QPushButton:
        btn = QPushButton()
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setFixedHeight(42)

        # Internal Layout for Icon + Text (+ Chevron)
        layout = QHBoxLayout(btn)
        layout.setContentsMargins(12, 0, 12, 0)
        layout.setSpacing(12)

        # Icon
        icon_lbl = QLabel()
        icon = qta.icon(icon_name, color="white")
        icon_lbl.setPixmap(icon.pixmap(18, 18))
        icon_lbl.setStyleSheet("background: transparent; border: none;")
        icon_lbl.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        layout.addWidget(icon_lbl)

        # Text Label
        text_lbl = QLabel(title)
        text_lbl.setStyleSheet("background: transparent; border: none; color: #FFFFFF; font-size: 13.5px; font-weight: 500;")
        text_lbl.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        layout.addWidget(text_lbl, 1)

        # Chevron Icon >
        if has_chevron:
            chev_lbl = QLabel()
            chev_icon = qta.icon("fa5s.chevron-right", color="white")
            chev_lbl.setPixmap(chev_icon.pixmap(10, 10))
            chev_lbl.setStyleSheet("background: transparent; border: none;")
            chev_lbl.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
            layout.addWidget(chev_lbl)

        btn.clicked.connect(lambda _, idx=index, t=title: self.on_button_clicked(idx, t))
        return btn

    def on_button_clicked(self, index: int, title: str):
        self.set_active_item(index)
        self.item_selected.emit(index, title)

    def set_active_item(self, index: int):
        self.current_active_index = index
        for i, btn in enumerate(self.nav_buttons):
            if i == index:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #1752A1;
                        border-radius: 8px;
                        border: none;
                    }
                    QPushButton:hover {
                        background-color: #1A5CB3;
                    }
                """)
            else:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border-radius: 8px;
                        border: none;
                    }
                    QPushButton:hover {
                        background-color: #0C325B;
                    }
                """)
