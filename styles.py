# Theme styling for EC - Budget & Bills Management System

MAIN_STYLE = """
QMainWindow {
    background-color: #F8FAFC;
}

/* ---------------------------------------------------------------------
   LEFT SIDEBAR STYLING (Dark Navy Theme)
   --------------------------------------------------------------------- */
SidebarWidget, QWidget#SidebarContainer {
    background-color: #03162A;
    border-right: 1px solid #082038;
}

/* Hide or polish scrollbar in Sidebar */
QScrollArea {
    border: none;
    background-color: transparent;
}

QScrollArea > QWidget > QWidget {
    background-color: transparent;
}

QScrollBar:vertical {
    border: none;
    background: transparent;
    width: 4px;
    margin: 0px;
}

QScrollBar::handle:vertical {
    background: rgba(255, 255, 255, 0.15);
    min-height: 20px;
    border-radius: 2px;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0px;
}

/* DDO Card Styling */
QFrame#DDOInfoCard {
    background-color: rgba(4, 25, 48, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 8px;
}

QLabel#DDOTitle {
    color: #FFFFFF;
    font-size: 13px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

QLabel#DDOCodeLabel {
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 600;
}

QLabel#DDOCodeValue {
    color: #FFFFFF;
    font-size: 16px;
    font-weight: bold;
}

QLabel#DDOCentralLabel {
    color: #FFFFFF;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 0.5px;
}

QFrame#VDivider {
    background-color: rgba(255, 255, 255, 0.2);
    width: 1px;
    border: none;
}

/* Bottom Footer Styling */
QFrame#HDivider {
    background-color: rgba(255, 255, 255, 0.2);
    max-height: 1px;
    min-height: 1px;
    border: none;
}

QLabel#FinYearTitle {
    color: #94A3B8;
    font-size: 11px;
    font-weight: 500;
}

QLabel#FinYearValue {
    color: #FFFFFF;
    font-size: 14px;
    font-weight: bold;
}

QFrame#CalendarBox {
    border: 1px solid rgba(255, 255, 255, 0.3);
    border-radius: 6px;
    background-color: transparent;
}


/* ---------------------------------------------------------------------
   RIGHT MAIN CONTENT AREA STYLING (Executive Light Dashboard)
   --------------------------------------------------------------------- */
QWidget#MainContentArea {
    background-color: #F8FAFC;
}

/* Top Header Bar */
QFrame#TopHeaderBar {
    background-color: #FFFFFF;
    border-bottom: 1px solid #E2E8F0;
}

QLabel#HeaderOrgTitle {
    color: #0F172A;
    font-size: 15px;
    font-weight: bold;
}

QLabel#HeaderOrgSub {
    color: #2563EB;
    font-size: 12px;
    font-weight: 600;
}

QComboBox#FinYearCombo {
    background-color: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    padding: 4px 10px;
    color: #1E293B;
    font-weight: 600;
    font-size: 13px;
    min-width: 110px;
}

QComboBox#FinYearCombo::drop-down {
    border: none;
    width: 20px;
}

/* Dashboard Header */
QLabel#DashboardTitle {
    color: #0F172A;
    font-size: 20px;
    font-weight: bold;
}

QLabel#DashboardSub {
    color: #64748B;
    font-size: 13px;
}

/* KPI Summary Cards */
QFrame#KPICard {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
}

QLabel#KPICardTitle {
    color: #64748B;
    font-size: 12px;
    font-weight: 600;
}

QLabel#KPICardValue {
    font-size: 17px;
    font-weight: bold;
}

QLabel#KPICardFooter {
    color: #94A3B8;
    font-size: 11px;
}

/* Main Section Containers (Budget Summary & Recent Bills) */
QFrame#SectionCard {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
}

QLabel#SectionHeader {
    color: #0F172A;
    font-size: 15px;
    font-weight: bold;
}

/* Table Styling */
QTableWidget#CustomTable {
    background-color: transparent;
    border: none;
    gridline-color: #F1F5F9;
    font-size: 12px;
}

QTableWidget#CustomTable::item {
    padding: 6px 4px;
    color: #334155;
}

QHeaderView::section {
    background-color: #F8FAFC;
    color: #475569;
    font-weight: bold;
    font-size: 11.5px;
    border: none;
    border-bottom: 1px solid #E2E8F0;
    padding: 6px 4px;
}

/* Link Button */
QPushButton#LinkButton {
    color: #2563EB;
    font-size: 12.5px;
    font-weight: 600;
    border: none;
    background: transparent;
    text-align: left;
}

QPushButton#LinkButton:hover {
    text-decoration: underline;
}

/* Progress Bar */
QProgressBar {
    border: none;
    background-color: #E2E8F0;
    border-radius: 4px;
    height: 6px;
    text-align: center;
}

QProgressBar::chunk {
    background-color: #2563EB;
    border-radius: 4px;
}
"""
