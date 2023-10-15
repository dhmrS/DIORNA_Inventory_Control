# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUITjUOuY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(681, 400)
        Form.setMinimumSize(QSize(681, 400))
        Form.setMaximumSize(QSize(681, 400))
        Form.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.pantalla = QTabWidget(Form)
        self.pantalla.setObjectName(u"pantalla")
        self.pantalla.setGeometry(QRect(0, 0, 681, 400))
        self.pantalla.setMinimumSize(QSize(681, 400))
        self.pantalla.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"QPushButton{\n"
"	border: 2px solid #8f8f91;  /* Define el color del borde y el grosor */\n"
"    border-radius: 10px;  /* Define el radio del borde, cuanto mayor el n\u00famero, m\u00e1s redondeado */\n"
"}\n"
"\n"
"QLabel{\n"
"	font: 16pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"")
        self.pantalla.setTabPosition(QTabWidget.North)
        self.pantalla.setTabShape(QTabWidget.Triangular)
        self.pantalla.setIconSize(QSize(16, 16))
        self.pantalla.setElideMode(Qt.ElideLeft)
        self.pantalla.setUsesScrollButtons(True)
        self.pantalla.setMovable(False)
        self.todos_los_productos = QWidget()
        self.todos_los_productos.setObjectName(u"todos_los_productos")
        self.todos_los_productos.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.todos_los_productos)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabla_productos = QTableWidget(self.todos_los_productos)
        if (self.tabla_productos.columnCount() < 5):
            self.tabla_productos.setColumnCount(5)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        __qtablewidgetitem.setBackground(QColor(255, 0, 191));
        self.tabla_productos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font);
        __qtablewidgetitem1.setBackground(QColor(85, 255, 127));
        self.tabla_productos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        __qtablewidgetitem2.setBackground(QColor(255, 248, 53));
        self.tabla_productos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font);
        __qtablewidgetitem3.setBackground(QColor(0, 170, 127));
        self.tabla_productos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font);
        __qtablewidgetitem4.setBackground(QColor(255, 170, 0));
        self.tabla_productos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabla_productos.setObjectName(u"tabla_productos")
        self.tabla_productos.setRowCount(0)
        self.tabla_productos.setColumnCount(5)

        self.horizontalLayout_3.addWidget(self.tabla_productos)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.bt_refrescar = QPushButton(self.todos_los_productos)
        self.bt_refrescar.setObjectName(u"bt_refrescar")
        self.bt_refrescar.setMinimumSize(QSize(0, 0))
        self.bt_refrescar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"border: 2px solid #0b0b0b;  /* Define el color del borde y el grosor */\n"
"border-radius: 5px;  /* Define el radio del borde, cuanto mayor el n\u00famero, m\u00e1s redondeado */\n"
"")

        self.verticalLayout_5.addWidget(self.bt_refrescar)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.label_14 = QLabel(self.todos_los_productos)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.label_14.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.label_14)

        self.pantalla.addTab(self.todos_los_productos, "")
        self.buscar_producto = QWidget()
        self.buscar_producto.setObjectName(u"buscar_producto")
        self.verticalLayout_6 = QVBoxLayout(self.buscar_producto)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_Nombre_de_producto = QLabel(self.buscar_producto)
        self.label_Nombre_de_producto.setObjectName(u"label_Nombre_de_producto")

        self.horizontalLayout_4.addWidget(self.label_Nombre_de_producto)

        self.codigoB = QLineEdit(self.buscar_producto)
        self.codigoB.setObjectName(u"codigoB")

        self.horizontalLayout_4.addWidget(self.codigoB)

        self.bt_buscar = QPushButton(self.buscar_producto)
        self.bt_buscar.setObjectName(u"bt_buscar")
        self.bt_buscar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"border: 2px solid #0b0b0b;  /* Define el color del borde y el grosor */\n"
"border-radius: 5px;  /* Define el radio del borde, cuanto mayor el n\u00famero, m\u00e1s redondeado */")

        self.horizontalLayout_4.addWidget(self.bt_buscar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.tabla_buscar = QTableWidget(self.buscar_producto)
        if (self.tabla_buscar.columnCount() < 5):
            self.tabla_buscar.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font);
        __qtablewidgetitem5.setBackground(QColor(255, 0, 191));
        self.tabla_buscar.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font);
        __qtablewidgetitem6.setBackground(QColor(85, 255, 127));
        self.tabla_buscar.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font);
        __qtablewidgetitem7.setBackground(QColor(255, 248, 53));
        self.tabla_buscar.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font);
        __qtablewidgetitem8.setBackground(QColor(0, 170, 127));
        self.tabla_buscar.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font);
        __qtablewidgetitem9.setBackground(QColor(255, 170, 0));
        self.tabla_buscar.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tabla_buscar.setObjectName(u"tabla_buscar")
        self.tabla_buscar.setRowCount(0)
        self.tabla_buscar.setColumnCount(5)

        self.verticalLayout_6.addWidget(self.tabla_buscar)

        self.label_15 = QLabel(self.buscar_producto)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_15)

        self.pantalla.addTab(self.buscar_producto, "")
        self.add_producto = QWidget()
        self.add_producto.setObjectName(u"add_producto")
        self.verticalLayout_2 = QVBoxLayout(self.add_producto)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.add_producto)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.codigoA = QLineEdit(self.add_producto)
        self.codigoA.setObjectName(u"codigoA")

        self.horizontalLayout.addWidget(self.codigoA)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.add_producto)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_5.addWidget(self.label_3)

        self.nombreA = QLineEdit(self.add_producto)
        self.nombreA.setObjectName(u"nombreA")

        self.horizontalLayout_5.addWidget(self.nombreA)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.add_producto)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.modeloA = QLineEdit(self.add_producto)
        self.modeloA.setObjectName(u"modeloA")

        self.horizontalLayout_6.addWidget(self.modeloA)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.add_producto)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.precioA = QLineEdit(self.add_producto)
        self.precioA.setObjectName(u"precioA")

        self.horizontalLayout_7.addWidget(self.precioA)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.add_producto)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.cantidadA = QLineEdit(self.add_producto)
        self.cantidadA.setObjectName(u"cantidadA")

        self.horizontalLayout_12.addWidget(self.cantidadA)


        self.verticalLayout.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_13.addLayout(self.verticalLayout)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.bt_agregar = QPushButton(self.add_producto)
        self.bt_agregar.setObjectName(u"bt_agregar")
        self.bt_agregar.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"\n"
"border: 2px solid #0b0b0b;  /* Define el color del borde y el grosor */\n"
"border-radius: 5px;  /* Define el radio del borde, cuanto mayor el n\u00famero, m\u00e1s redondeado */")

        self.verticalLayout_8.addWidget(self.bt_agregar)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.l_agregar_producto_nuevo = QLabel(self.add_producto)
        self.l_agregar_producto_nuevo.setObjectName(u"l_agregar_producto_nuevo")
        self.l_agregar_producto_nuevo.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.l_agregar_producto_nuevo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.l_agregar_producto_nuevo)

        self.pantalla.addTab(self.add_producto, "")
        self.mod_producto = QWidget()
        self.mod_producto.setObjectName(u"mod_producto")
        self.verticalLayout_10 = QVBoxLayout(self.mod_producto)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.mod_producto)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_8.addWidget(self.label_13)

        self.id_producto = QLineEdit(self.mod_producto)
        self.id_producto.setObjectName(u"id_producto")

        self.horizontalLayout_8.addWidget(self.id_producto)

        self.id_buscar = QPushButton(self.mod_producto)
        self.id_buscar.setObjectName(u"id_buscar")
        self.id_buscar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.id_buscar)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(2, 0, 0, 0)
        self.label_7 = QLabel(self.mod_producto)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_4.addWidget(self.label_7)

        self.label_8 = QLabel(self.mod_producto)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_4.addWidget(self.label_8)

        self.label_9 = QLabel(self.mod_producto)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_4.addWidget(self.label_9)

        self.label_10 = QLabel(self.mod_producto)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_4.addWidget(self.label_10)

        self.label_11 = QLabel(self.mod_producto)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_4.addWidget(self.label_11)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.codigo_actualizar = QLineEdit(self.mod_producto)
        self.codigo_actualizar.setObjectName(u"codigo_actualizar")

        self.verticalLayout_3.addWidget(self.codigo_actualizar)

        self.nombre_actualizar = QLineEdit(self.mod_producto)
        self.nombre_actualizar.setObjectName(u"nombre_actualizar")

        self.verticalLayout_3.addWidget(self.nombre_actualizar)

        self.modelo_actualizar = QLineEdit(self.mod_producto)
        self.modelo_actualizar.setObjectName(u"modelo_actualizar")

        self.verticalLayout_3.addWidget(self.modelo_actualizar)

        self.precio_actualizar = QLineEdit(self.mod_producto)
        self.precio_actualizar.setObjectName(u"precio_actualizar")

        self.verticalLayout_3.addWidget(self.precio_actualizar)

        self.cantidad_actualizar = QLineEdit(self.mod_producto)
        self.cantidad_actualizar.setObjectName(u"cantidad_actualizar")

        self.verticalLayout_3.addWidget(self.cantidad_actualizar)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_7)

        self.bt_actualizar = QPushButton(self.mod_producto)
        self.bt_actualizar.setObjectName(u"bt_actualizar")
        self.bt_actualizar.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 255, 0);\n"
"color: rgb(0, 0, 0);\n"
"")

        self.verticalLayout_9.addWidget(self.bt_actualizar)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_9)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.l_modificar_producto = QLabel(self.mod_producto)
        self.l_modificar_producto.setObjectName(u"l_modificar_producto")
        self.l_modificar_producto.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.l_modificar_producto.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.l_modificar_producto)

        self.pantalla.addTab(self.mod_producto, "")
        self.borrar_producto = QWidget()
        self.borrar_producto.setObjectName(u"borrar_producto")
        self.verticalLayout_12 = QVBoxLayout(self.borrar_producto)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.borrar_producto)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.codigo_borrar = QLineEdit(self.borrar_producto)
        self.codigo_borrar.setObjectName(u"codigo_borrar")

        self.horizontalLayout_10.addWidget(self.codigo_borrar)

        self.borrar_ok = QPushButton(self.borrar_producto)
        self.borrar_ok.setObjectName(u"borrar_ok")
        self.borrar_ok.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.borrar_ok)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.tabla_borrar = QTableWidget(self.borrar_producto)
        if (self.tabla_borrar.columnCount() < 5):
            self.tabla_borrar.setColumnCount(5)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font);
        __qtablewidgetitem10.setBackground(QColor(255, 0, 191));
        self.tabla_borrar.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font);
        __qtablewidgetitem11.setBackground(QColor(85, 255, 127));
        self.tabla_borrar.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font);
        __qtablewidgetitem12.setBackground(QColor(255, 248, 53));
        self.tabla_borrar.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font);
        __qtablewidgetitem13.setBackground(QColor(0, 170, 127));
        self.tabla_borrar.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font);
        __qtablewidgetitem14.setBackground(QColor(255, 170, 0));
        self.tabla_borrar.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tabla_borrar.setObjectName(u"tabla_borrar")
        self.tabla_borrar.setRowCount(0)
        self.tabla_borrar.setColumnCount(5)

        self.horizontalLayout_11.addWidget(self.tabla_borrar)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_9)

        self.bt_borrar = QPushButton(self.borrar_producto)
        self.bt_borrar.setObjectName(u"bt_borrar")
        self.bt_borrar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout_11.addWidget(self.bt_borrar)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_11)


        self.verticalLayout_12.addLayout(self.horizontalLayout_11)

        self.label_18 = QLabel(self.borrar_producto)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18)

        self.pantalla.addTab(self.borrar_producto, "")

        self.retranslateUi(Form)

        self.pantalla.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"REGISTRO DE PRODUCTOS", None))
#if QT_CONFIG(statustip)
        self.todos_los_productos.setStatusTip("")
#endif // QT_CONFIG(statustip)
        ___qtablewidgetitem = self.tabla_productos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem1 = self.tabla_productos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla_productos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Modelo", None));
        ___qtablewidgetitem3 = self.tabla_productos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Precio", None));
        ___qtablewidgetitem4 = self.tabla_productos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Cantidad", None));
        self.bt_refrescar.setText(QCoreApplication.translate("Form", u"REFRESCAR", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"VER TODOS LOS PRODUCTOS", None))
        self.pantalla.setTabText(self.pantalla.indexOf(self.todos_los_productos), QCoreApplication.translate("Form", u"PRODUCTOS", None))
        self.label_Nombre_de_producto.setText(QCoreApplication.translate("Form", u"NOMBRE DEL PRODUCTO", None))
        self.codigoB.setText("")
        self.bt_buscar.setText(QCoreApplication.translate("Form", u"BUSCAR", None))
        ___qtablewidgetitem5 = self.tabla_buscar.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem6 = self.tabla_buscar.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem7 = self.tabla_buscar.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Modelo", None));
        ___qtablewidgetitem8 = self.tabla_buscar.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Precio", None));
        ___qtablewidgetitem9 = self.tabla_buscar.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Cantidad", None));
        self.label_15.setText(QCoreApplication.translate("Form", u"BUSCAR UN PRODUCTO", None))
        self.pantalla.setTabText(self.pantalla.indexOf(self.buscar_producto), QCoreApplication.translate("Form", u"BUSCAR  PRODUCTO", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"CODIGO:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"NOMBRE:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"MODELO:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"PRECIO: ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"CANTIDAD: ", None))
        self.bt_agregar.setText(QCoreApplication.translate("Form", u"AGREGAR", None))
        self.l_agregar_producto_nuevo.setText(QCoreApplication.translate("Form", u"AGREGAR UN PRODUCTO NUEVO", None))
        self.pantalla.setTabText(self.pantalla.indexOf(self.add_producto), QCoreApplication.translate("Form", u"AGREGAR NUEVOS PRODUCTOS", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"INGRESE EL C\u00d3DIGO DEL PRODUCTO", None))
        self.id_buscar.setText(QCoreApplication.translate("Form", u"BUSCAR", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"CODIGO:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"NOMBRE:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"MODELO:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"PRECIO: ", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"CANTIDAD: ", None))
        self.bt_actualizar.setText(QCoreApplication.translate("Form", u"MODIFICAR", None))
        self.l_modificar_producto.setText(QCoreApplication.translate("Form", u"MODIFICAR UN PRODUCTO EXISTENTE", None))
        self.pantalla.setTabText(self.pantalla.indexOf(self.mod_producto), QCoreApplication.translate("Form", u"ACTUALIZAR PRODUCTOS", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"CODIGO:", None))
        self.codigo_borrar.setText("")
        self.borrar_ok.setText(QCoreApplication.translate("Form", u"BUSCAR", None))
        ___qtablewidgetitem10 = self.tabla_borrar.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Codigo", None));
        ___qtablewidgetitem11 = self.tabla_borrar.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem12 = self.tabla_borrar.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Modelo", None));
        ___qtablewidgetitem13 = self.tabla_borrar.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Precio", None));
        ___qtablewidgetitem14 = self.tabla_borrar.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Cantidad", None));
        self.bt_borrar.setText(QCoreApplication.translate("Form", u"ELIMINAR", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"ELIMINAR UN PRODUCTO", None))
        self.pantalla.setTabText(self.pantalla.indexOf(self.borrar_producto), QCoreApplication.translate("Form", u"BORRAR PRODUCTOS", None))
    # retranslateUi

