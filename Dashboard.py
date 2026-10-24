import sys
from pathlib import Path
from PyQt6.QtCore import Qt, QRectF, QSize
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QMainWindow,
    QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QStackedWidget, QInputDialog, QComboBox, QScrollArea
)
from PyQt6.QtGui import QPainter, QPen, QColor, QFont, QIcon, QPixmap, QPainterPath


class FlatIconPainter:
    """Draws clean, flat 2D vector icons directly in code matching reference designs."""

    @staticmethod
    def draw_washing_machine(size=32, color="#ffffff"):
        """1. Washing Machine Icon for Dashboard."""
        pix = QPixmap(size, size)
        pix.fill(Qt.GlobalColor.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        main_color = QColor(color)
        pen = QPen(main_color, 2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        p.setPen(pen)
        p.setBrush(main_color)

        # Main Solid Washing Machine Outer Body (Rounded Rectangle)
        p.drawRoundedRect(QRectF(3, 3, 26, 26), 5, 5)

        # Top Control Panel Separator Line (Cutout)
        p.setPen(QPen(QColor(0, 0, 0, 0), 0))
        p.setBrush(QColor("#a4beda"))
        p.drawRect(QRectF(3, 9, 26, 1.5))

        # Top Panel Details (Cutout slot line & two dots)
        p.drawRoundedRect(QRectF(6, 5.5, 9, 1.8), 0.9, 0.9)
        p.drawEllipse(QRectF(19, 5, 2.5, 2.5))
        p.drawEllipse(QRectF(23, 5, 2.5, 2.5))

        # Center Circular Door Ring
        p.setBrush(main_color)
        p.setPen(pen)
        p.drawEllipse(QRectF(8, 12, 16, 16))

        # Inner Drum Fill & Water Wave Cutout
        p.setBrush(QColor("#a4beda"))
        p.setPen(QPen(QColor("#a4beda"), 1))
        
        drum_path = QPainterPath()
        drum_path.addEllipse(QRectF(10, 14, 12, 12))
        
        water_wave = QPainterPath()
        water_wave.moveTo(10, 20)
        water_wave.cubicTo(13, 17.5, 17, 22, 22, 19.5)
        water_wave.lineTo(22, 26)
        water_wave.lineTo(10, 26)
        water_wave.closeSubpath()
        
        final_water = drum_path.intersected(water_wave)
        p.drawPath(final_water)
        p.end()
        return QIcon(pix)

    @staticmethod
    def draw_document(size=32, color="#ffffff"):
        """2. Document / Receipt Icon for Transactions."""
        pix = QPixmap(size, size)
        pix.fill(Qt.GlobalColor.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        main_color = QColor(color)
        pen = QPen(main_color, 2.2, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        p.setPen(pen)
        p.setBrush(main_color)

        # Document Outline with Scalloped Bottom
        path = QPainterPath()
        path.moveTo(6, 4)
        path.lineTo(26, 4)
        path.lineTo(26, 25)
        path.cubicTo(24, 28, 22, 25, 20, 28)
        path.cubicTo(18, 25, 16, 28, 14, 25)
        path.cubicTo(12, 28, 10, 25, 8, 28)
        path.cubicTo(7, 26, 6, 26, 6, 25)
        path.closeSubpath()
        p.drawPath(path)

        # Bullet Points & Text Bars Cutout
        p.setBrush(QColor("#a4beda"))
        p.setPen(QPen(QColor(0, 0, 0, 0), 0))
        p.drawEllipse(QRectF(9.5, 8, 3, 3))
        p.drawRoundedRect(QRectF(15, 8.5, 7, 2), 1, 1)
        p.drawEllipse(QRectF(9.5, 14, 3, 3))
        p.drawRoundedRect(QRectF(15, 14.5, 7, 2), 1, 1)
        p.drawEllipse(QRectF(9.5, 20, 3, 3))
        p.drawRoundedRect(QRectF(15, 20.5, 7, 2), 1, 1)
        p.end()
        return QIcon(pix)

    @staticmethod
    def draw_info(size=32, color="#ffffff"):
        """3. Info Circle Icon for About Page."""
        pix = QPixmap(size, size)
        pix.fill(Qt.GlobalColor.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        main_color = QColor(color)
        pen = QPen(main_color, 2.4, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap)
        p.setPen(pen)
        p.setBrush(main_color)

        # Outer Circle
        p.drawEllipse(QRectF(3, 3, 26, 26))
        
        # Info Dot & Pillar Cutout
        p.setBrush(QColor("#a4beda"))
        p.setPen(QPen(QColor(0, 0, 0, 0), 0))
        p.drawEllipse(QRectF(14.5, 8, 3, 3))
        p.drawRoundedRect(QRectF(14, 14, 4, 10), 2, 2)
        p.end()
        return QIcon(pix)

    @staticmethod
    def draw_exit(size=32, color="#ffffff"):
        """4. Exit Door Icon."""
        pix = QPixmap(size, size)
        pix.fill(Qt.GlobalColor.transparent)
        p = QPainter(pix)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        main_color = QColor(color)
        pen = QPen(main_color, 2.4, Qt.PenStyle.SolidLine, Qt.PenCapStyle.RoundCap, Qt.PenJoinStyle.RoundJoin)
        p.setPen(pen)

        # Door Frame Outline with Opening
        door_path = QPainterPath()
        door_path.moveTo(11, 13)
        door_path.lineTo(11, 6)
        door_path.lineTo(26, 6)
        door_path.lineTo(26, 26)
        door_path.lineTo(11, 26)
        door_path.lineTo(11, 20)
        p.drawPath(door_path)

        # Exit Arrow
        p.drawLine(5, 16, 21, 16)
        p.drawLine(16, 11, 21, 16)
        p.drawLine(16, 21, 21, 16)
        p.end()
        return QIcon(pix)


class StatusDot(QWidget):
    """Status dot indicator."""
    def __init__(self, color="#6fd36f", size=22):
        super().__init__()
        self._color = QColor(color)
        self.setFixedSize(size, size)

    def set_color(self, color):
        self._color = QColor(color)
        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        p.setPen(QPen(self._color.darker(115), 2))
        p.setBrush(self._color)
        p.drawEllipse(QRectF(self.rect()).adjusted(2, 2, -2, -2))


class WasherWidget(QWidget):
    """Washer circular icon with ring and inner fill."""
    def __init__(self, ring="#c8cfd8", fill="#b8f2ff", ring_width=14):
        super().__init__()
        self._ring = QColor(ring)
        self._fill = QColor(fill)
        self._w = ring_width
        self.setMinimumSize(110, 110)

    def sizeHint(self):
        return QSize(140, 140)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        p.setPen(QPen(self._ring, self._w))
        p.setBrush(self._fill)
        side = min(self.width(), self.height()) - self._w
        x = (self.width() - side) / 2
        y = (self.height() - side) / 2
        p.drawEllipse(QRectF(x, y, side, side))


class CustomerCard(QWidget):
    """Card representing a customer washer position."""
    def __init__(self, name="CUSTOMER #1", status_color="#6fd36f", is_unoccupied=False, data=None):
        super().__init__()
        self.is_unoccupied = is_unoccupied
        self.data = data or {
            "name": name,
            "status": "For Pick-up",
            "personal_name": "Jane Doe",
            "contact": "+1 234 567 890",
            "weight": "5.5 kg",
            "garments": "12",
            "add_ons": ["Fabric Softener", "Extra Rinse"],
            "delivery": "Pick-Up",
            "service_fee": "$15.00",
            "addons_fee": "$3.00"
        }

        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.status = StatusDot(color=status_color)
        self.name_label = QLabel(name.upper())
        self.name_label.setObjectName("customer_name_label")

        self.line = QFrame()
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setObjectName("card_line")

        if is_unoccupied:
            self.washer = WasherWidget(ring="#555555", fill="#2d2d2d")
        else:
            self.washer = WasherWidget(ring="#c8cfd8", fill="#b8f2ff")

        layout = QGridLayout()
        layout.addWidget(self.status, 0, 0)
        layout.addWidget(self.name_label, 0, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.line, 1, 0, 1, 2)
        layout.addWidget(self.washer, 2, 0, 1, 2, Qt.AlignmentFlag.AlignCenter)
        layout.setColumnStretch(1, 1)
        self.setLayout(layout)


class TransactionCard(QWidget):
    """Expandable transaction history card."""
    def __init__(self, customer_name, total_amount, booking_date, service_date, received_date, details):
        super().__init__()
        self.setObjectName("tx_card")

        main_layout = QVBoxLayout(self)

        top_layout = QHBoxLayout()
        left_layout = QVBoxLayout()

        name_lbl = QLabel(customer_name)
        name_lbl.setObjectName("tx_name")
        left_layout.addWidget(name_lbl)

        booking_lbl = QLabel(f"Day of Booking: {booking_date}")
        booking_lbl.setObjectName("tx_date")
        service_lbl = QLabel(f"Day of Service: {service_date}")
        service_lbl.setObjectName("tx_date")
        received_lbl = QLabel(f"Date Received: {received_date}")
        received_lbl.setObjectName("tx_date")

        left_layout.addWidget(booking_lbl)
        left_layout.addWidget(service_lbl)
        left_layout.addWidget(received_lbl)

        amount_lbl = QLabel(f"${total_amount:.2f}")
        amount_lbl.setObjectName("tx_amount")

        top_layout.addLayout(left_layout)
        top_layout.addStretch()
        top_layout.addWidget(amount_lbl, alignment=Qt.AlignmentFlag.AlignTop)

        main_layout.addLayout(top_layout)

        self.toggle_btn = QPushButton("▲ Hide details")
        self.toggle_btn.setObjectName("tx_toggle_btn")
        self.toggle_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        main_layout.addWidget(self.toggle_btn)

        self.details_widget = QWidget()
        details_layout = QVBoxLayout(self.details_widget)
        details_layout.setContentsMargins(0, 5, 0, 0)

        tx_title = QLabel("Transaction Details")
        tx_title.setObjectName("section_heading")
        details_layout.addWidget(tx_title)

        for key, val in details.items():
            row = QHBoxLayout()
            k_lbl = QLabel(f"{key}" + "." * (40 - len(key)))
            k_lbl.setObjectName("info_label")
            v_lbl = QLabel(f"${val:.2f}")
            v_lbl.setObjectName("info_label")
            row.addWidget(k_lbl)
            row.addStretch()
            row.addWidget(v_lbl)
            details_layout.addLayout(row)

        tot_row = QHBoxLayout()
        tot_k = QLabel("Total:")
        tot_k.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        tot_v = QLabel(f"${total_amount:.2f}")
        tot_v.setFont(QFont("Segoe UI", 10, QFont.Weight.Bold))
        tot_row.addStretch()
        tot_row.addWidget(tot_k)
        tot_row.addWidget(tot_v)
        details_layout.addLayout(tot_row)

        main_layout.addWidget(self.details_widget)
        self.toggle_btn.clicked.connect(self.toggle_details)

    def toggle_details(self):
        if self.details_widget.isVisible():
            self.details_widget.hide()
            self.toggle_btn.setText("▼ More details")
        else:
            self.details_widget.show()
            self.toggle_btn.setText("▲ Hide details")


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Dashboard System")
        self.resize(1000, 650)

        self.cards = []

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ===== 1. LEFT SIDEBAR =====
        sidebar_frame = QFrame()
        sidebar_frame.setObjectName("sidebar_container")
        sidebar_frame.setFixedWidth(75)

        sidebar_layout = QVBoxLayout(sidebar_frame)
        sidebar_layout.setContentsMargins(10, 25, 10, 25)
        sidebar_layout.setSpacing(15)

        def create_btn(icon):
            btn = QPushButton()
            btn.setObjectName("nav_btn")
            btn.setFixedSize(50, 50)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setIcon(icon)
            btn.setIconSize(QSize(32, 32))
            return btn

        self.btn_dashboard = create_btn(FlatIconPainter.draw_washing_machine(32, "#ffffff"))
        self.btn_transactions = create_btn(FlatIconPainter.draw_document(32, "#ffffff"))
        self.btn_about = create_btn(FlatIconPainter.draw_info(32, "#ffffff"))
        self.btn_exit = create_btn(FlatIconPainter.draw_exit(32, "#ffffff"))

        sidebar_line = QFrame()
        sidebar_line.setFrameShape(QFrame.Shape.HLine)
        sidebar_line.setObjectName("sidebar_divider")
        sidebar_line.setFixedWidth(36)

        sidebar_layout.addWidget(self.btn_dashboard, alignment=Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(sidebar_line, alignment=Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(self.btn_transactions, alignment=Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addStretch()
        sidebar_layout.addWidget(self.btn_about, alignment=Qt.AlignmentFlag.AlignCenter)
        sidebar_layout.addWidget(self.btn_exit, alignment=Qt.AlignmentFlag.AlignCenter)

        # ===== 2. CENTRAL STACKED PAGES =====
        self.stacked_widget = QStackedWidget()

        # --- PAGE 0: DASHBOARD PAGE ---
        dashboard_page = QWidget()
        dash_page_layout = QVBoxLayout(dashboard_page)
        dash_page_layout.setContentsMargins(20, 20, 20, 20)

        header_layout = QHBoxLayout()
        header_title = QLabel("DASHBOARD")
        header_title.setObjectName("header_title")

        self.add_appt_btn = QPushButton("+  Add Appointment")
        self.add_appt_btn.setObjectName("addApptBtn")
        self.add_appt_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        header_layout.addWidget(header_title)
        header_layout.addStretch()
        header_layout.addWidget(self.add_appt_btn)

        queue_info_layout = QVBoxLayout()
        queue_lbl = QLabel("Washes In Queue")
        queue_lbl.setObjectName("queue_title")
        self.total_lbl = QLabel("In total: 3 / 4")
        self.total_lbl.setObjectName("queue_subtext")
        queue_info_layout.addWidget(queue_lbl)
        queue_info_layout.addWidget(self.total_lbl)

        self.grid_container = QFrame()
        self.grid_container.setObjectName("cards_container")
        self.grid_layout = QGridLayout(self.grid_container)
        self.grid_layout.setSpacing(20)

        dash_page_layout.addLayout(header_layout)
        dash_page_layout.addLayout(queue_info_layout)
        dash_page_layout.addWidget(self.grid_container, stretch=1)

        # --- PAGE 1: TRANSACTIONS PAGE ---
        transactions_page = QWidget()
        tx_page_layout = QVBoxLayout(transactions_page)
        tx_page_layout.setContentsMargins(20, 20, 20, 20)

        tx_header = QLabel("TRANSACTION HISTORY")
        tx_header.setObjectName("header_title")
        tx_page_layout.addWidget(tx_header)

        tx_scroll = QScrollArea()
        tx_scroll.setWidgetResizable(True)
        tx_scroll.setFrameShape(QFrame.Shape.NoFrame)
        tx_scroll_content = QWidget()
        self.tx_list_layout = QVBoxLayout(tx_scroll_content)
        self.tx_list_layout.setSpacing(15)

        tx1 = TransactionCard(
            "Customer #2 Name", 9999.99, "MM/DD/YYYY", "MM/DD/YYYY", "MM/DD/YYYY",
            {"Transit Fee": 10.00, "Service Fee": 50.00, "Add-ons": 15.00, "VAT": 5.00}
        )
        tx2 = TransactionCard(
            "Customer #1 Name", 9999.99, "MM/DD/YYYY", "MM/DD/YYYY", "MM/DD/YYYY",
            {"Transit Fee": 12.00, "Service Fee": 45.00, "Add-ons": 10.00, "VAT": 4.50}
        )
        tx2.toggle_details()

        self.tx_list_layout.addWidget(tx1)
        self.tx_list_layout.addWidget(tx2)
        self.tx_list_layout.addStretch()

        tx_scroll.setWidget(tx_scroll_content)
        tx_page_layout.addWidget(tx_scroll)

        # --- PAGE 2: ABOUT PAGE ---
        about_page = QWidget()
        about_layout = QVBoxLayout(about_page)
        about_title = QLabel("ABOUT SYSTEM")
        about_title.setObjectName("header_title")
        about_desc = QLabel("Laundry Management Dashboard Application v1.0")
        about_desc.setObjectName("info_label")
        about_layout.addWidget(about_title)
        about_layout.addWidget(about_desc)
        about_layout.addStretch()

        self.stacked_widget.addWidget(dashboard_page)
        self.stacked_widget.addWidget(transactions_page)
        self.stacked_widget.addWidget(about_page)

        # ===== 3. RIGHT DETAILS PANEL =====
        self.details_panel = QFrame()
        self.details_panel.setObjectName("details_container")
        self.details_panel.setFixedWidth(280)

        self.details_layout = QVBoxLayout(self.details_panel)
        self.details_layout.setContentsMargins(20, 20, 20, 20)

        self.placeholder_lbl = QLabel("Select a\nwasher to\nview details")
        self.placeholder_lbl.setObjectName("details_placeholder")
        self.placeholder_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.details_layout.addWidget(self.placeholder_lbl)

        self.details_content = QWidget()
        self.details_content_layout = QVBoxLayout(self.details_content)
        self.details_content_layout.setContentsMargins(0, 0, 0, 0)
        self.details_content.hide()
        self.details_layout.addWidget(self.details_content)

        main_layout.addWidget(sidebar_frame)
        main_layout.addWidget(self.stacked_widget, stretch=1)
        main_layout.addWidget(self.details_panel)

        self.btn_dashboard.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.btn_transactions.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.btn_about.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(2))
        self.btn_exit.clicked.connect(self.close)

        self.add_appt_btn.clicked.connect(self.add_appointment)

        self.init_cards()

    def init_cards(self):
        initial_cards = [
            CustomerCard("CUSTOMER #1", "#6fd36f"),
            CustomerCard("CUSTOMER #2", "#e6b800"),
            CustomerCard("CUSTOMER #3", "#e64d4d"),
            CustomerCard("UNOCCUPIED", "#555555", is_unoccupied=True)
        ]
        for card in initial_cards:
            self.add_card_to_grid(card)

    def add_card_to_grid(self, card):
        index = len(self.cards)
        row = index // 2
        col = index % 2
        self.grid_layout.addWidget(card, row, col)
        self.cards.append(card)

        card.mousePressEvent = lambda event, c=card: self.show_card_details(c)
        self.update_queue_label()

    def show_card_details(self, card):
        self.placeholder_lbl.hide()
        self.details_content.show()

        while self.details_content_layout.count():
            item = self.details_content_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        d = card.data

        cust_header = QLabel(d["name"])
        cust_header.setObjectName("details_customer_header")
        self.details_content_layout.addWidget(cust_header, alignment=Qt.AlignmentFlag.AlignRight)

        status_box = QComboBox()
        status_box.setObjectName("status_combobox")
        status_box.addItems(["For Pick-up", "In Progress", "Completed", "Cancelled"])
        status_box.setCurrentText(d["status"])
        self.details_content_layout.addWidget(status_box)

        lbl_pi = QLabel("Personal Information")
        lbl_pi.setObjectName("section_heading")
        lbl_name = QLabel(f"Name:\n{d['personal_name']}")
        lbl_name.setObjectName("info_label")
        lbl_contact = QLabel(f"Contact Number:\n{d['contact']}")
        lbl_contact.setObjectName("info_label")

        self.details_content_layout.addWidget(lbl_pi)
        self.details_content_layout.addWidget(lbl_name)
        self.details_content_layout.addWidget(lbl_contact)

        lbl_ld = QLabel("Laundry Details")
        lbl_ld.setObjectName("section_heading")
        lbl_weight = QLabel(f"Weight (kg):\n{d['weight']}")
        lbl_weight.setObjectName("info_label")
        lbl_garments = QLabel(f"# of Garments:\n{d['garments']}")
        lbl_garments.setObjectName("info_label")
        lbl_addons = QLabel("Add-ons:\n• " + "\n• ".join(d["add_ons"]))
        lbl_addons.setObjectName("info_label")

        self.details_content_layout.addWidget(lbl_ld)
        self.details_content_layout.addWidget(lbl_weight)
        self.details_content_layout.addWidget(lbl_garments)
        self.details_content_layout.addWidget(lbl_addons)

        lbl_del_head = QLabel("Delivery")
        lbl_del_head.setObjectName("section_heading")
        lbl_del = QLabel(f"Delivery Option:\n{d['delivery']}")
        lbl_del.setObjectName("info_label")

        self.details_content_layout.addWidget(lbl_del_head)
        self.details_content_layout.addWidget(lbl_del)

        lbl_tx_head = QLabel("Transaction Details")
        lbl_tx_head.setObjectName("section_heading")
        lbl_service = QLabel(f"Service Fee: {d['service_fee']}")
        lbl_service.setObjectName("info_label")
        lbl_addons_fee = QLabel(f"Add-ons Fee: {d['addons_fee']}")
        lbl_addons_fee.setObjectName("info_label")

        self.details_content_layout.addWidget(lbl_tx_head)
        self.details_content_layout.addWidget(lbl_service)
        self.details_content_layout.addWidget(lbl_addons_fee)

        self.details_content_layout.addStretch()

    def add_appointment(self):
        default_name = f"CUSTOMER #{len(self.cards) + 1}"
        name, ok = QInputDialog.getText(self, "Add Appointment", "Enter Customer Name:", text=default_name)
        if ok and name.strip():
            new_card = CustomerCard(name.strip().upper(), "#6fd36f")
            self.add_card_to_grid(new_card)

    def update_queue_label(self):
        active_count = sum(1 for c in self.cards if not c.is_unoccupied)
        self.total_lbl.setText(f"In total: {active_count} / {len(self.cards)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qss_path = Path(__file__).with_name("Dashboard_style.qss")
    if qss_path.exists():
        app.setStyleSheet(qss_path.read_text())

    window = Dashboard()
    window.show()
    sys.exit(app.exec())