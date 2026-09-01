import qtawesome as qta
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QPushButton,
    QProgressBar
)

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(24, 20, 24, 20)
        main_layout.setSpacing(20)

        # ----------------------------------------------------
        # 1. Top Header Bar (ECP Logo + Org Title + Right Controls)
        # ----------------------------------------------------
        top_header_card = QFrame()
        top_header_card.setObjectName("TopHeaderBar")
        top_header_card.setStyleSheet("background-color: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 8px;")
        header_layout = QHBoxLayout(top_header_card)
        header_layout.setContentsMargins(16, 12, 16, 12)
        header_layout.setSpacing(14)

        # Left: ECP Emblem Icon + Titles
        left_header = QHBoxLayout()
        left_header.setSpacing(12)

        # Emblem Icon (Green Circle with Emblem)
        emblem_box = QFrame()
        emblem_box.setFixedSize(40, 40)
        emblem_box.setStyleSheet("background-color: #16A34A; border-radius: 20px;")
        emblem_layout = QVBoxLayout(emblem_box)
        emblem_layout.setContentsMargins(0, 0, 0, 0)
        emblem_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        emblem_icon_lbl = QLabel()
        emblem_icon = qta.icon("fa5s.university", color="white")
        emblem_icon_lbl.setPixmap(emblem_icon.pixmap(22, 22))
        emblem_icon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        emblem_layout.addWidget(emblem_icon_lbl)

        left_header.addWidget(emblem_box)

        # Title Text Block
        org_title_box = QVBoxLayout()
        org_title_box.setSpacing(1)

        lbl_org_main = QLabel("Election Commission of Pakistan")
        lbl_org_main.setObjectName("HeaderOrgTitle")

        lbl_org_sub = QLabel("Bills & Budget Management System")
        lbl_org_sub.setObjectName("HeaderOrgSub")

        org_title_box.addWidget(lbl_org_main)
        org_title_box.addWidget(lbl_org_sub)
        left_header.addLayout(org_title_box)

        header_layout.addLayout(left_header)
        header_layout.addStretch()

        # Right: Financial Year Dropdown + DEO Profile
        right_header = QHBoxLayout()
        right_header.setSpacing(18)

        # Financial Year Combo Box
        fin_year_box = QHBoxLayout()
        fin_year_box.setSpacing(8)
        lbl_fin_label = QLabel("Financial Year")
        lbl_fin_label.setStyleSheet("color: #475569; font-size: 13px; font-weight: 500;")

        combo_fin = QComboBox()
        combo_fin.setObjectName("FinYearCombo")
        combo_fin.addItems(["2026 - 2027", "2025 - 2026", "2024 - 2025"])

        fin_year_box.addWidget(lbl_fin_label)
        fin_year_box.addWidget(combo_fin)
        right_header.addLayout(fin_year_box)

        # User Profile Badge
        user_badge_box = QHBoxLayout()
        user_badge_box.setSpacing(8)

        user_icon_lbl = QLabel()
        user_icon = qta.icon("fa5s.user-circle", color="#2563EB")
        user_icon_lbl.setPixmap(user_icon.pixmap(30, 30))
        user_badge_box.addWidget(user_icon_lbl)

        user_txt_box = QVBoxLayout()
        user_txt_box.setSpacing(0)

        lbl_user_name = QLabel("DEO")
        lbl_user_name.setStyleSheet("color: #0F172A; font-size: 13px; font-weight: bold;")

        lbl_user_role = QLabel("Logged in as DEO")
        lbl_user_role.setStyleSheet("color: #64748B; font-size: 11px;")

        user_txt_box.addWidget(lbl_user_name)
        user_txt_box.addWidget(lbl_user_role)
        user_badge_box.addLayout(user_txt_box)

        right_header.addLayout(user_badge_box)
        header_layout.addLayout(right_header)

        main_layout.addWidget(top_header_card)

        # ----------------------------------------------------
        # 2. Dashboard Title Section
        # ----------------------------------------------------
        title_box = QVBoxLayout()
        title_box.setSpacing(2)

        lbl_dash_title = QLabel("Dashboard")
        lbl_dash_title.setObjectName("DashboardTitle")

        lbl_dash_sub = QLabel("Overview of Budget, Expenditure and Bills")
        lbl_dash_sub.setObjectName("DashboardSub")

        title_box.addWidget(lbl_dash_title)
        title_box.addWidget(lbl_dash_sub)
        main_layout.addLayout(title_box)

        # ----------------------------------------------------
        # 3. Top 5 KPI Metric Cards Row
        # ----------------------------------------------------
        kpi_row_layout = QHBoxLayout()
        kpi_row_layout.setSpacing(14)

        cards_data = [
            ("Total Budget Allocated", "Rs.444,000", "Across All Heads", "fa5s.wallet", "#16A34A"),
            ("Total Expenditure", "Rs.0", "Up to Date", "fa5s.chart-bar", "#1D4ED8"),
            ("Remaining Balance", "Rs.444,000", "Available Balance", "fa5s.file-invoice-dollar", "#EA580C"),
            ("Number of Bills", "0", "This Financial Year", "fa5s.file-alt", "#7C3AED"),
            ("Pending Bills", "0", "Awaiting Approval", "fa5s.clock", "#DC2626")
        ]

        for title, val, footer_txt, icon_str, color_hex in cards_data:
            card = QFrame()
            card.setObjectName("KPICard")
            card_layout = QHBoxLayout(card)
            card_layout.setContentsMargins(12, 12, 12, 12)
            card_layout.setSpacing(10)

            # Icon Box
            icon_box = QFrame()
            icon_box.setFixedSize(40, 40)
            icon_box.setStyleSheet(f"background-color: {color_hex}; border-radius: 8px;")
            ib_layout = QVBoxLayout(icon_box)
            ib_layout.setContentsMargins(0, 0, 0, 0)
            ib_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

            ic_lbl = QLabel()
            ic = qta.icon(icon_str, color="white")
            ic_lbl.setPixmap(ic.pixmap(18, 18))
            ib_layout.addWidget(ic_lbl)

            card_layout.addWidget(icon_box)

            # Text Info
            info_box = QVBoxLayout()
            info_box.setSpacing(2)

            lbl_t = QLabel(title)
            lbl_t.setObjectName("KPICardTitle")

            lbl_v = QLabel(val)
            lbl_v.setObjectName("KPICardValue")
            lbl_v.setStyleSheet(f"color: {color_hex}; font-size: 15px; font-weight: bold;")

            lbl_f = QLabel(footer_txt)
            lbl_f.setObjectName("KPICardFooter")

            info_box.addWidget(lbl_t)
            info_box.addWidget(lbl_v)
            info_box.addWidget(lbl_f)

            card_layout.addLayout(info_box, 1)
            kpi_row_layout.addWidget(card)

        main_layout.addLayout(kpi_row_layout)

        # ----------------------------------------------------
        # 4. Main Content Cards (Budget Utilization | Recent Bills)
        # ----------------------------------------------------
        split_layout = QHBoxLayout()
        split_layout.setSpacing(16)

        # ------------------------------------
        # LEFT CARD: Budget Utilization Summary
        # ------------------------------------
        budget_card = QFrame()
        budget_card.setObjectName("SectionCard")
        b_layout = QVBoxLayout(budget_card)
        b_layout.setContentsMargins(16, 16, 16, 14)
        b_layout.setSpacing(12)

        lbl_b_header = QLabel("Budget Utilization Summary")
        lbl_b_header.setObjectName("SectionHeader")
        b_layout.addWidget(lbl_b_header)

        # Table Widget
        b_table = QTableWidget()
        b_table.setObjectName("CustomTable")
        b_table.setColumnCount(5)
        b_table.setHorizontalHeaderLabels(["Object Classification", "Budget Allocated", "Expenditure", "Balance", "Utilization"])
        
        header = b_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        
        b_table.verticalHeader().setVisible(False)
        b_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        b_table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)

        rows_data = [
            ("A-01277 Contingent Paid Staff", "Rs.444,000", "Rs.0", "Rs.444,000", 0),
            ("A-03001 Conveyance Charges", "-", "-", "-", 0),
            ("A-03201 Stationery", "-", "-", "-", 0),
            ("A-03202 Conferences / Seminars", "-", "-", "-", 0),
            ("A-03205 Newspapers, Periodicals", "-", "-", "-", 0),
        ]

        b_table.setRowCount(len(rows_data))
        for row_idx, (code, alloc, exp, bal, util) in enumerate(rows_data):
            # Code
            item_code = QTableWidgetItem(code)
            b_table.setItem(row_idx, 0, item_code)

            # Allocated
            item_alloc = QTableWidgetItem(alloc)
            item_alloc.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            b_table.setItem(row_idx, 1, item_alloc)

            # Expenditure
            item_exp = QTableWidgetItem(exp)
            item_exp.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            b_table.setItem(row_idx, 2, item_exp)

            # Balance
            item_bal = QTableWidgetItem(bal)
            item_bal.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            b_table.setItem(row_idx, 3, item_bal)

            # Progress Bar for Utilization
            p_container = QWidget()
            p_layout = QHBoxLayout(p_container)
            p_layout.setContentsMargins(2, 0, 2, 0)
            p_layout.setSpacing(4)

            lbl_p_text = QLabel(f"{util}%")
            lbl_p_text.setStyleSheet("color: #475569; font-size: 11px; font-weight: 500;")

            p_bar = QProgressBar()
            p_bar.setRange(0, 100)
            p_bar.setValue(util)
            p_bar.setFixedHeight(6)

            p_layout.addWidget(lbl_p_text)
            p_layout.addWidget(p_bar, 1)

            b_table.setCellWidget(row_idx, 4, p_container)

        b_layout.addWidget(b_table, 1)

        # Footer Link
        btn_b_report = QPushButton("View Full Budget Report  >")
        btn_b_report.setObjectName("LinkButton")
        b_layout.addWidget(btn_b_report)

        split_layout.addWidget(budget_card, 1)

        # ------------------------------------
        # RIGHT CARD: Recent Bills
        # ------------------------------------
        bills_card = QFrame()
        bills_card.setObjectName("SectionCard")
        bills_layout = QVBoxLayout(bills_card)
        bills_layout.setContentsMargins(16, 16, 16, 14)
        bills_layout.setSpacing(12)

        lbl_bills_header = QLabel("Recent Bills")
        lbl_bills_header.setObjectName("SectionHeader")
        bills_layout.addWidget(lbl_bills_header)

        # Empty State Content
        empty_container = QWidget()
        empty_layout = QVBoxLayout(empty_container)
        empty_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        empty_layout.setSpacing(8)

        empty_icon_lbl = QLabel()
        empty_icon = qta.icon("fa5s.file-alt", color="#CBD5E1")
        empty_icon_lbl.setPixmap(empty_icon.pixmap(52, 52))
        empty_icon_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_no_bills = QLabel("No Bills Found")
        lbl_no_bills.setStyleSheet("color: #64748B; font-size: 15px; font-weight: bold;")
        lbl_no_bills.setAlignment(Qt.AlignmentFlag.AlignCenter)

        lbl_sub_bills = QLabel("Create a new bill to get started.")
        lbl_sub_bills.setStyleSheet("color: #94A3B8; font-size: 13px;")
        lbl_sub_bills.setAlignment(Qt.AlignmentFlag.AlignCenter)

        empty_layout.addWidget(empty_icon_lbl)
        empty_layout.addWidget(lbl_no_bills)
        empty_layout.addWidget(lbl_sub_bills)

        bills_layout.addWidget(empty_container, 1)

        # Footer Link
        btn_bills_link = QPushButton("View All Bills  >")
        btn_bills_link.setObjectName("LinkButton")
        btn_bills_link.setStyleSheet("text-align: right;")
        bills_layout.addWidget(btn_bills_link, 0, Qt.AlignmentFlag.AlignRight)

        split_layout.addWidget(bills_card, 1)

        main_layout.addLayout(split_layout, 1)
