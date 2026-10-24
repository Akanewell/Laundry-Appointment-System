import sys, os
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QMainWindow,
                             QGridLayout, QPushButton, QVBoxLayout,
                             QHBoxLayout, QFrame, QComboBox, QStackedLayout, QStackedWidget)

from PyQt6.QtGui import QIcon
from pathlib import Path
from Washer_button import CustomerCard


class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laundry Dashboard System")
        self.setFixedSize(800, 527)

        # ===== Buttons =====

        # ----- sidebar -----
        self.dashboard_btn = QPushButton()
        self.dashboard_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        dashboard_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Btn icons/1.png")
        self.dashboard_btn.setIcon(QIcon(dashboard_icon_path))
        self.dashboard_btn.setIconSize(QSize(60,60))
        self.dashboard_btn.setFlat(True)
        self.dashboard_btn.setToolTip("Dashboard")

        self.transaction_btn = QPushButton()
        self.transaction_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        transaction_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Btn icons/2.png")
        self.transaction_btn.setIcon(QIcon(transaction_icon_path))
        self.transaction_btn.setIconSize(QSize(60,60))
        self.transaction_btn.setFlat(True)
        self.transaction_btn.setToolTip("Transaction")

        self.about_btn = QPushButton()
        self.about_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        about_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Btn icons/3.png")
        self.about_btn.setIcon(QIcon(about_icon_path))
        self.about_btn.setIconSize(QSize(60,60))
        self.about_btn.setFlat(True)
        self.about_btn.setToolTip("About")

        self.exit_btn = QPushButton()
        self.exit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        exit_icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Btn icons/4.png")
        self.exit_btn.setIcon(QIcon(exit_icon_path))
        self.exit_btn.setIconSize(QSize(60,60))
        self.exit_btn.setFlat(True)
        self.exit_btn.setToolTip("About")
        
        #self.dashboard_btn.clicked.connect()
        #self.dashboard_btn.clicked.connect()
        #self.dashboard_btn.clicked.connect()
        self.exit_btn.clicked.connect(self.close)

        # ----- dashboard -----
        self.header = QLabel("Dashboard")
        self.add_appointment_btn = QPushButton("+ Add Appointment")
        self.add_appointment_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.add_appointment_btn.setFixedSize(200, 40)

        self.inQueue_text = QLabel("Washes in Queue")
        self.total_text = QLabel("Total: 0 / 0")

        # ----- details -----
        self.details_placeholder = QLabel("Select a washer to view details")
        self.details_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.customer_details_name = QLabel("Customer #1")
        #self.statusDropdown = QComboBox()
        

        # ===== Layout =====

        main_layout = QHBoxLayout()  # whole app
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)
        
        # ----- sidebar (left) -----
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.dashboard_btn)
        sidebar_layout.addWidget(self.transaction_btn)
        sidebar_layout.addWidget(self.about_btn)
        sidebar_layout.addWidget(self.exit_btn)

        sidebar_container = QFrame()
        sidebar_container.setLayout(sidebar_layout)

        # ----- dashboard (middle) -----
        dashboard_layout = QVBoxLayout()
        header_layout = QHBoxLayout()
        washers_layout = QVBoxLayout()    # washers text info + customers
        customers_layout = QGridLayout()  # the whole grid of customers

        customers_container = QFrame()
        customers_container.setLayout(customers_layout)

        header_layout.addWidget(self.header)
        header_layout.addWidget(self.add_appointment_btn)

        #testing [NOT FINAL]
        names = ["Customer #1", "Customer #2", "Customer #3", "Customer #4", "Customer #5"]
        for i, name in enumerate(names):
            customers_layout.addWidget(CustomerCard(name), i // 2, i % 2)


        washers_layout.addWidget(self.inQueue_text, stretch=0)
        washers_layout.addWidget(self.total_text, stretch=0)
        washers_layout.addWidget(customers_container, stretch=1)

        dashboard_layout.addLayout(header_layout)
        dashboard_layout.addLayout(washers_layout)

        # ----- details (right) -----
        details_layout = QVBoxLayout()
        details_layout.addWidget(self.details_placeholder)

        details_container = QFrame()
        details_container.setLayout(details_layout)

        # ----- add sections to main -----
        main_layout.addWidget(sidebar_container, stretch=0)
        main_layout.addLayout(dashboard_layout, stretch= 2)
        main_layout.addWidget(details_container, stretch=1)  # not details_layout.addLayout(details_layout)

        self.setLayout(main_layout)

        # ===== setObjectName & Others =====
        self.header.setObjectName("header")
        self.add_appointment_btn.setObjectName("addApptBtn")
        self.inQueue_text.setObjectName("inQueue_text")
        self.total_text.setObjectName("total_text")
        customers_container.setObjectName("customers_layout")
        details_container.setObjectName("details_layout")
        sidebar_container.setObjectName("sidebar_layout")
        self.details_placeholder.setObjectName("details_placeholder")

        self.dashboard_btn.setObjectName("dashboard_btn")
        self.transaction_btn.setObjectName("transaction_btn")
        self.about_btn.setObjectName("about_btn")
        self.exit_btn.setObjectName("exit_btn")
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dashboard_qss = Path(__file__).with_name("Dashboard_style.qss")
    app.setStyleSheet(Dashboard_qss.read_text())
    window = Dashboard()
    window.show()
    sys.exit(app.exec())