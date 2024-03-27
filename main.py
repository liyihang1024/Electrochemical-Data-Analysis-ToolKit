import re
import os
import sys
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QMdiSubWindow, QFileDialog, QMessageBox, QPlainTextEdit, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
from PySide6.QtCore import QThread, Slot
from PySide6.QtGui import QPainter, QPixmap, QIcon, QFontMetrics
from PySide6.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Ui_main import Ui_MainWindow  # 替换为您的主窗口 UI 类
from Ui_FunctionWindow import Ui_MainWindow as Ui_FunctionWindow  # 替换为您的子窗口 UI 类
import matplotlib
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.sans-serif'] = ['Microsoft YaHei']

class FunctionWindow(QMainWindow, Ui_FunctionWindow):
    def __init__(self, parent=None):
        super(FunctionWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义常量
        self.electrode_area  = float(self.lineEdit_electrode_area.text() )  # 电极面积，单位为cm²
        self.potential_shift = float(self.lineEdit_potential_shift.text())  # 电压转换到RHE的偏移值

        # 为frame_TafelSlope添加垂直布局
        self.frame_TafelSlope.setLayout(QVBoxLayout())
        
        # 添加CV数据存储
        self.fileNames_CV = []
        self.data_CV = []

        # 设置标志来追踪按钮的状态（False表示当前为导入数据状态）
        self.isDataImported_CV = False

        # 连接CV相关按钮的信号
        self.btn_addData_CV.clicked.connect(self.addData_CV)
        self.btn_importData_CV.clicked.connect(self.importData_CV)
        self.btn_Plot_CV.clicked.connect(self.plotData_CV)
        self.btn_saveData_CV.clicked.connect(self.saveData_CV)


        # 添加LSV数据存储
        self.fileNames_LSV = []
        self.data_LSV = []

        # 设置标志来追踪按钮的状态（False表示当前为导入数据状态）
        self.isDataImported_LSV = False

        # 连接LSV相关按钮的信号
        self.btn_addData_LSV.clicked.connect(self.addData_LSV)
        self.btn_importData_LSV.clicked.connect(self.importData_LSV)
        self.btn_Plot_LSV.clicked.connect(self.plotData_LSV)
        self.btn_saveData_LSV.clicked.connect(self.saveData_LSV)


        # 添加Cdl数据存储
        self.data_Cdl = []
        self.fileGroups_Cdl = []  # 初始化文件组列表

        # 初始化一个空的 list 用于存储所有处理后的Cdl电势和电流密度数据用于后续导出
        self.list_Cdl_data = []

        # 将处理后的阳极和阴极电流密度信息保存用于后续导出
        self.summary_df_Cdl = None

        # 设置标志来追踪按钮的状态（False表示当前为导入数据状态）
        self.isDataImported_Cdl = False

        # 连接Cdl相关按钮的信号
        self.btn_addData_Cdl.clicked.connect(self.addData_Cdl)
        self.btn_importData_Cdl.clicked.connect(self.importData_Cdl)
        self.btn_Plot_Cdl.clicked.connect(self.plotData_Cdl)
        self.btn_saveData_Cdl.clicked.connect(self.saveData_Cdl)


        # 添加 Tafel 数据存储
        self.fileNames_Tafel = []
        self.data_Tafel = []

        # 设置标志来追踪按钮的状态（False表示当前为导入数据状态）
        self.isDataImported_Tafel = False

        # 连接 Tafel 相关按钮的信号
        self.btn_addData_Tafel.clicked.connect(self.addData_Tafel)
        self.btn_importData_Tafel.clicked.connect(self.importData_Tafel)
        self.btn_Plot_Tafel.clicked.connect(self.plotData_Tafel)
        self.btn_saveData_Tafel.clicked.connect(self.saveData_Tafel)

    def adjustPlainTextEditHeight(self, plainTextEdit: QPlainTextEdit, minHeight=72):
        # 获取文本框的字体度量信息
        fontMetrics = QFontMetrics(plainTextEdit.font())
        # 计算文本所需的行数
        text = plainTextEdit.toPlainText()
        lineCount = text.count('\n') + 1 if text else 1
        # 计算文本框所需的高度
        newHeight = max(fontMetrics.lineSpacing() * lineCount + 2 * plainTextEdit.frameWidth(), minHeight)

        # 设置文本框的最小和最大高度
        plainTextEdit.setMinimumHeight(newHeight + 10)
        plainTextEdit.setMaximumHeight(newHeight + 10)

############################# CV模块：开始 #############################
    def addData_CV(self):
        files, _ = QFileDialog.getOpenFileNames(self, "选择Excel文件", "", "Excel文件 (*.xlsx *.xls)")
        if files:
            self.fileNames_CV.extend(files)
            # 将新文件路径添加到文本框中
            current_text = self.plainTextEdit_CV_Data.toPlainText()
            new_text = "\n".join(files) if not current_text else current_text + "\n" + "\n".join(files)
            self.plainTextEdit_CV_Data.setPlainText(new_text)

            # 将每组数据的父文件夹名保存在 plainTextEdit_CV_Label 中
            for file in files:
                folder_name = os.path.basename(os.path.dirname(file))  # 获取父文件夹名
                current_label_text = self.plainTextEdit_CV_Label.toPlainText()
                new_label_text = folder_name if not current_label_text else current_label_text + "\n" + folder_name
                self.plainTextEdit_CV_Label.setPlainText(new_label_text)

            # 调整文本框高度以显示所有内容
            self.adjustPlainTextEditHeight(self.plainTextEdit_CV_Data)
            self.adjustPlainTextEditHeight(self.plainTextEdit_CV_Label)

    def importData_CV(self):
        if self.isDataImported_CV:  # 如果数据已导入，则清除数据
            self.clearData_CV()
            return
        
        if not self.fileNames_CV:  # 检查是否已添加文件
            QMessageBox.warning(self, "警告", "请先添加文件！")
            return
        
        # 这里应该在子线程中执行
        for file in self.fileNames_CV:
            data = pd.read_excel(file, index_col=None, header=0)
            self.data_CV.append(data)
        
        # 数据导入后显示弹窗提醒
        QMessageBox.information(self, "导入数据", "CV数据已成功导入！")

        # 数据导入成功后
        self.isDataImported_CV = True
        self.btn_importData_CV.setText("清除数据")

    def clearData_CV(self):
        # 清除存储的数据和文件名
        self.data_CV.clear()
        self.fileNames_CV.clear()

        # 清空文本框
        self.plainTextEdit_CV_Data.setPlainText("")
        self.plainTextEdit_CV_Label.setPlainText("")

        # 设置文本框的默认高度
        self.adjustPlainTextEditHeight(self.plainTextEdit_CV_Data, minHeight=72)
        self.adjustPlainTextEditHeight(self.plainTextEdit_CV_Label, minHeight=72)

        # 恢复按钮文字并重置状态标志
        self.btn_importData_CV.setText("导入数据")
        self.isDataImported_CV = False

    def plotData_CV(self):
        if not self.data_CV:  # 检查是否已导入数据
            QMessageBox.warning(self, "警告", "请先导入数据！")
            return

        # 根据导入的数据表数量确定行列数
        num_plots = len(self.data_CV)
        ncols = min(num_plots, 3)
        nrows = num_plots // ncols + (1 if num_plots % ncols else 0)

        fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(5 * ncols, 4 * nrows), constrained_layout=True)

        # 如果只有一个图，确保 axes 是一个列表
        if num_plots == 1:
            axes = [axes]

        # 适应多个子图的情况
        if num_plots > 1:
            axes = axes.flatten()

        # 使用 plainTextEdit_CV_Label 中的每行内容作为标签
        label_text = self.plainTextEdit_CV_Label.toPlainText().split("\n")

        for ax, data, label in zip(axes, self.data_CV, label_text):
            # 计算不同扫描（Scan）的数量
            scans = data['Scan'].unique()

            # 定义颜色映射
            color_map = matplotlib.colormaps.get_cmap('jet')
            colors = [color_map(i / len(scans)) for i in range(len(scans))]
            
            # 按扫描编号绘制每一圈的数据
            for i, scan in enumerate(scans):
                scan_data = data[data['Scan'] == scan]
                potential = scan_data['WE(1).Potential (V)'] + self.potential_shift      # 转换为RHE电势
                current   = scan_data['WE(1).Current (A)'] * 1000 / self.electrode_area  # 转换为电流密度

                # 将第一个元素复制并添加到列表末尾
                potential = pd.concat([potential, pd.Series([potential.iloc[0]])], ignore_index=True)
                current = pd.concat([current, pd.Series([current.iloc[0]])], ignore_index=True)

                # 循环绘制每一圈的数据
                
                # 只在循环的第一次迭代中设置图例标签
                if i == 0:
                    ax.plot(potential, current, color=colors[i], label=label)
                else:
                    ax.plot(potential, current, color=colors[i])

            # 设置坐标轴标签
            ax.set_xlabel("Potential (V vs. RHE)")
            ax.set_ylabel("Current density (mA/cm²)")

            # 添加网格
            ax.grid(True, linestyle='--')

            # 设置图例
            legend = ax.legend(loc='best', frameon=False, shadow=False)

            # 从legend对象中获取句柄
            handles = legend.legend_handles
            # 单独设置每个句柄的颜色
            handles[0].set_color('white')

            # 触发渲染过程以初始化渲染器
            plt.gcf().canvas.draw()

            # 获取图例的像素坐标
            legend_fig_coord = legend.get_window_extent().get_points()

            # 获取图形的尺寸（英寸）
            size_inches = fig.get_size_inches()

            # 获取图形的DPI
            dpi = fig.dpi

            # 计算图形的尺寸（像素）
            width_pixels = size_inches[0] * dpi
            height_pixels = size_inches[1] * dpi

            # 创建颜色条
            norm = mpl.colors.Normalize(vmin=scans.min(), vmax=scans.max())
            sm = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
            sm.set_array([])
            # 创建专门用于颜色条的Axes对象，并指定位置和大小
            # 根据转换后的坐标调整颜色条的位置和大小
            cbar_left = legend_fig_coord[0][0]/width_pixels+0.01
            cbar_bottom = legend_fig_coord[0][1]/height_pixels-0.03
            cbar_width = 0.08
            cbar_height = 0.02
            cbar_ax = fig.add_axes([cbar_left, cbar_bottom, cbar_width, cbar_height])
            cbar = plt.colorbar(sm, cax=cbar_ax, orientation='horizontal')
            cbar.set_label('Scan')
            cbar.set_ticks([scans.min(), scans.max()])  # 设置颜色条上的刻度为最小和最大扫描数
            cbar.set_ticklabels([str(scans.min()), str(scans.max())])  # 设置对应的标签

        # 绘图
        plt.show()

    def saveData_CV(self):
        # 检查是否已导入数据
        if not self.data_CV:
            QMessageBox.warning(self, "警告", "没有数据可保存！")
            return

        # 询问用户保存文件的位置
        save_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "data_CV", "Excel Files (*.xlsx)")
        if not save_path:
            return  # 用户取消了保存

        # 使用 plainTextEdit_CV_Label 中的每行内容作为标签
        sample_text = self.plainTextEdit_CV_Label.toPlainText().split("\n")

        # 创建一个Pandas ExcelWriter对象
        with pd.ExcelWriter(save_path) as writer:
            for sample, data in zip(sample_text, self.data_CV):
                # 数据处理
                potential_RHE = data['WE(1).Potential (V)'] + self.potential_shift  # 转换为RHE电势
                current_density = data['WE(1).Current (A)'] * 1000 / self.electrode_area  # 转换为电流密度

                # 创建要保存的DataFrame
                df_to_save = pd.DataFrame({
                    'Potential (V vs. RHE)': potential_RHE,
                    'Current density (mA/cm²)': current_density
                })

                # 获取文件名作为sheet名（去掉路径和扩展名）
                # 修改：使用与plotData_CV中相同的方式提取文件名作为sheet名
                sheet_name = sample

                # 将数据写入Excel文件的对应sheet
                df_to_save.to_excel(writer, sheet_name=sheet_name, index=False)

        QMessageBox.information(self, "保存数据", "CV数据已成功保存！")
############################# CV模块：结束 #############################

############################# LSV模块：开始 #############################
    # LSV数据添加方法
    def addData_LSV(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Excel Files", "", "Excel Files (*.xlsx *.xls)")
        if files:
            self.fileNames_LSV.extend(files)
            # 将新文件路径添加到文本框中
            current_text = self.plainTextEdit_LSV_Data.toPlainText()
            new_text = "\n".join(files) if not current_text else current_text + "\n" + "\n".join(files)
            self.plainTextEdit_LSV_Data.setPlainText(new_text)

            # 将每组数据的父文件夹名保存在 plainTextEdit_LSV_Label 中
            for file in files:
                folder_name = os.path.basename(os.path.dirname(file))  # 获取父文件夹名
                current_label_text = self.plainTextEdit_LSV_Label.toPlainText()
                new_label_text = folder_name if not current_label_text else current_label_text + "\n" + folder_name
                self.plainTextEdit_LSV_Label.setPlainText(new_label_text)

            # 调整文本框高度以显示所有内容
            self.adjustPlainTextEditHeight(self.plainTextEdit_LSV_Data)
            self.adjustPlainTextEditHeight(self.plainTextEdit_LSV_Label)

    # LSV数据导入方法
    def importData_LSV(self):
        if self.isDataImported_LSV:  # 如果数据已导入，则清除数据
            self.clearData_LSV()
            return
        
        if not self.fileNames_LSV:  # 检查是否已添加文件
            QMessageBox.warning(self, "警告", "请先添加文件！")
            return
        
        for file in self.fileNames_LSV:
            data = pd.read_excel(file, index_col=None, header=0)
            self.data_LSV.append(data)

        # 数据导入后显示弹窗提醒
        QMessageBox.information(self, "导入数据", "LSV数据已成功导入！")

        # 数据导入成功后
        self.isDataImported_LSV = True
        self.btn_importData_LSV.setText("清除数据")

    def clearData_LSV(self):
        # 清除存储的数据和文件名
        self.data_LSV.clear()
        self.fileNames_LSV.clear()

        # 清空文本框
        self.plainTextEdit_LSV_Data.setPlainText("")
        self.plainTextEdit_LSV_Label.setPlainText("")

        # 设置文本框的默认高度
        self.adjustPlainTextEditHeight(self.plainTextEdit_LSV_Data, minHeight=72)
        self.adjustPlainTextEditHeight(self.plainTextEdit_LSV_Label, minHeight=72)

        # 恢复按钮文字并重置状态标志
        self.btn_importData_LSV.setText("导入数据")
        self.isDataImported_LSV = False

    # LSV绘图方法
    def plotData_LSV(self):
        if not self.data_LSV:
            QMessageBox.warning(self, "警告", "请先导入数据！")
            return

        # 创建一个包含两个子图的图形
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

        # 定义常量
        y_intercept = 10  # y = 10 的水平线

        bar_labels = []
        bar_values = []

        # 使用 plainTextEdit_LSV_Label 中的每行内容作为标签
        label_text = self.plainTextEdit_LSV_Label.toPlainText().split("\n")

        for data, label in zip(self.data_LSV, label_text):
            potential_RHE = data['WE(1).Potential (V)'] + self.potential_shift
            current_density = data['WE(1).Current (A)'] * 1000 / self.electrode_area

            # 绘制原始曲线
            ax1.plot(potential_RHE, current_density, label=label)

            # 将 Pandas Series 转换为 NumPy 数组
            current_density_np = current_density.to_numpy()
            potential_RHE_np = potential_RHE.to_numpy()

            # 寻找与 y = 10 交点的横坐标
            above = current_density_np > y_intercept
            below = current_density < y_intercept

            # 寻找曲线穿过 y=10 的点
            intersection_indices = np.where(above[:-1] != above[1:])[0]
            if intersection_indices.size > 0:
                # 获取穿过点的横坐标最大值
                max_intersection = potential_RHE_np[intersection_indices].max()
                overpotential = (max_intersection - 1.23) * 1000
                bar_labels.append(label)
                bar_values.append(overpotential)

        # 在第一个子图中添加 y = 10 的水平虚线
        ax1.axhline(y=y_intercept, color='gray', linestyle='--')

        ax1.set_xlabel("Potential (V vs. RHE)")
        ax1.set_ylabel("Current density (mA/cm²)")
        ax1.legend(loc='best', frameon=False, shadow=False)

        # 在第二个子图中绘制柱状图，调整柱子宽度并添加标签
        bar_width = 0.2  # 设置柱子的宽度
        bars = ax2.bar(bar_labels, bar_values, width=bar_width)

        # 确定 y 轴的最大值，以确保标签不超出边界
        max_bar_height = max(bar_values) if bar_values else 0
        ax2.set_ylim(0, max_bar_height + max_bar_height*0.1)  # 增加 10% 作为额外空间

        # 在每个柱子顶端添加高度标签
        for bar in bars:
            height = bar.get_height()
            ax2.annotate('{:.0f}'.format(height),
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

        ax2.set_xlabel("Sample")
        ax2.set_ylabel("Overpotential (mV)")

        plt.tight_layout()
        plt.show()

    def saveData_LSV(self):
        # 检查是否已导入数据
        if not self.data_LSV:
            QMessageBox.warning(self, "警告", "没有数据可保存！")
            return

        # 询问用户保存文件的位置
        save_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "data_LSV", "Excel Files (*.xlsx)")
        if not save_path:
            return  # 用户取消了保存

        # 使用 plainTextEdit_LSV_Label 中的每行内容作为标签
        sample_text = self.plainTextEdit_LSV_Label.toPlainText().split("\n")

        # 创建一个Pandas ExcelWriter对象
        with pd.ExcelWriter(save_path) as writer:
            for sample, data in zip(sample_text, self.data_LSV):
                # 数据处理
                potential_RHE = data['WE(1).Potential (V)'] + self.potential_shift  # 转换为RHE电势
                current_density = data['WE(1).Current (A)'] * 1000 / self.electrode_area  # 转换为电流密度

                # 创建要保存的DataFrame
                df_to_save = pd.DataFrame({
                    'Potential (V vs. RHE)': potential_RHE,
                    'Current density (mA/cm²)': current_density
                })

                # 获取文件名作为sheet名（去掉路径和扩展名）
                # 修改：使用与plotData_LSV中相同的方式提取文件名作为sheet名
                sheet_name = sample

                # 将数据写入Excel文件的对应sheet
                df_to_save.to_excel(writer, sheet_name=sheet_name, index=False)

        QMessageBox.information(self, "保存数据", "LSV数据已成功保存！")
############################# LSV模块：结束 #############################

############################# Cdl模块：开始 #############################
    # Cdl数据添加方法
    def addData_Cdl(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Excel Files", "", "Excel Files (*.xlsx *.xls)")
        if files:
            self.fileGroups_Cdl.append(files)  # 每次添加的文件作为一组
            # 更新UI以显示选择的文件
            current_text = self.plainTextEdit_Cdl_Data.toPlainText()
            
            new_text = "\n".join(files) if not current_text else current_text + "\n\n" + "\n".join(files)
            
            self.plainTextEdit_Cdl_Data.setPlainText(new_text)

            # 将每组数据的父文件夹名保存在 plainTextEdit_Cdl_Label 中
            folder_name = os.path.basename(os.path.dirname(files[0]))  # 获取父文件夹名
            current_label_text = self.plainTextEdit_Cdl_Label.toPlainText()

            if current_label_text:  # 检查是否为空
                new_label_text = current_label_text + "\n" + folder_name
            else:
                new_label_text = folder_name

            self.plainTextEdit_Cdl_Label.setPlainText(new_label_text)

            # 调整文本框高度以显示所有内容
            # self.adjustPlainTextEditHeight(self.plainTextEdit_Cdl_Data)
            # self.adjustPlainTextEditHeight(self.plainTextEdit_Cdl_Label)

    # Cdl数据导入方法
    def importData_Cdl(self):
        if self.isDataImported_Cdl:  # 如果数据已导入，则清除数据
            self.clearData_Cdl()
            return
        
        if not self.fileGroups_Cdl:  # 检查是否已添加文件
            QMessageBox.warning(self, "警告", "请先添加文件！")
            return
        
        for group in self.fileGroups_Cdl:
            group_data = [pd.read_excel(file, index_col=None, header=0) for file in group]
            self.data_Cdl.append(group_data)
        
        # 数据导入后显示弹窗提醒
        QMessageBox.information(self, "导入数据", "Cdl数据已成功导入！")

        # 数据导入成功后
        self.isDataImported_Cdl = True
        self.btn_importData_Cdl.setText("清除数据")

    def clearData_Cdl(self):
        # 清除存储的数据和文件名
        self.data_Cdl.clear()
        self.fileGroups_Cdl.clear()

        # 清空文本框
        self.plainTextEdit_Cdl_Data.setPlainText("")
        self.plainTextEdit_Cdl_Label.setPlainText("")

        # 设置文本框的默认高度
        self.adjustPlainTextEditHeight(self.plainTextEdit_Cdl_Data, minHeight=72)
        self.adjustPlainTextEditHeight(self.plainTextEdit_Cdl_Label, minHeight=72)

        # 恢复按钮文字并重置状态标志
        self.btn_importData_Cdl.setText("导入数据")
        self.isDataImported_Cdl = False
    
    # Cdl绘图方法
    def plotData_Cdl(self):
        if not self.data_Cdl:
            QMessageBox.warning(self, "警告", "请先导入数据！")
            return

        # 初始化 summary_df，指定数据类型
        summary_df = pd.DataFrame(columns=['Group', 'structure', 'Scan Rate (mV/s)', 'Anodic Current Density (mA/cm²)', 'Cathodic Current Density (mA/cm²)', 'Current Density Difference (mA/cm²)']).astype({
            'Group': 'int',
            'structure':'str',
            'Scan Rate (mV/s)':'int', 
            'Anodic Current Density (mA/cm²)': 'float',
            'Cathodic Current Density (mA/cm²)': 'float',
            'Current Density Difference (mA/cm²)': 'float'
        })


        # 确定子图的行列数
        num_groups = len(self.data_Cdl)
        nrows, ncols = (1, num_groups) if num_groups <= 3 else (-(-num_groups // 3), 3)

        # 创建不同扫速Cdl曲线子图
        fig, axs = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows), squeeze=False)
        axs = axs.flatten()

        # 使用 plainTextEdit_Cdl_Label 中的每行内容作为标签
        label_text = self.plainTextEdit_Cdl_Label.toPlainText().split("\n")
       
        # 遍历每组数据并在相应的子图中绘制
        for idx, (ax, group_data) in enumerate(zip(axs, self.data_Cdl)):
            scan_rates = []
            current_density_differences = []

            # 初始化一个空的 DataFrame 用于存储数据
            merged_data = pd.DataFrame()

            for file_path, data in zip(self.fileGroups_Cdl[idx], group_data):
                # 获取最后一个部分（文件名或最末级文件夹名）
                file_name = os.path.basename(file_path)

                # 提取扫描速率（从文件名中提取数字）
                scan_rate = int(re.search(r'\d+', file_name).group())
                scan_rates.append(scan_rate)

                # 筛选出最后倒数第二圈扫描的数据
                last_scan_number = data['Scan'].max() - 1
                last_scan_data = data[data['Scan'] == last_scan_number].copy()

                # 转换电压到RHE和电流到电流密度
                last_scan_data['Potential vs. RHE'] = last_scan_data['WE(1).Potential (V)'] + self.potential_shift
                last_scan_data['Current_Density_mA/cm2'] = last_scan_data['WE(1).Current (A)']*1000 / self.electrode_area

                # 计算电流密度差
                potential_midpoint = last_scan_data['Potential vs. RHE'].mean()
                midpoint_currents = last_scan_data.iloc[(last_scan_data['Potential vs. RHE'] - potential_midpoint).abs().argsort()[:2]]
                anodic_current_density = midpoint_currents['Current_Density_mA/cm2'].max()
                cathodic_current_density = midpoint_currents['Current_Density_mA/cm2'].min()
                current_density_difference = (anodic_current_density - cathodic_current_density) / 2
                current_density_differences.append(current_density_difference)

                new_row = pd.DataFrame({
                    'Group': [idx],
                    'structure':label_text[idx],
                    'Scan Rate (mV/s)':scan_rate,
                    'Anodic Current Density (mA/cm²)': [anodic_current_density],
                    'Cathodic Current Density (mA/cm²)': [cathodic_current_density],
                    'Current Density Difference (mA/cm²)': [current_density_difference]
                })
                summary_df = pd.concat([summary_df, new_row], ignore_index=True)

                # 复制第一行并添加到DataFrame的末尾用于绘制闭合曲线
                last_scan_data = pd.concat([last_scan_data, last_scan_data.iloc[[0]]], ignore_index=True)

                # 从 last_scan_data 中选择要合并的列，并将其添加到 merged_data 中
                selected_columns = ['Potential vs. RHE', 'Current_Density_mA/cm2']
                merged_data = pd.concat([merged_data, last_scan_data[selected_columns]], axis=1)

                # 绘制电流密度与电压的关系图
                ax.plot(last_scan_data['Potential vs. RHE'], last_scan_data['Current_Density_mA/cm2'], label=str(scan_rate) + " mV/s")
                ax.set_title(f"{label_text[idx]}")
                ax.set_xlabel("Potential (V vs. RHE)")
                ax.set_ylabel("Current Density (mA/cm²)")
                ax.legend(loc='best', frameon=False, shadow=False)
            
            # 将每组数据处理后的电势和电流密度保存
            self.list_Cdl_data.append(merged_data)
        
        # 将处理后的阳极和阴极电流密度信息保存用于后续导出
        self.summary_df_Cdl = summary_df

        # 隐藏多余的子图
        for ax in axs[num_groups:]:
            ax.set_visible(False)

        # 调整布局并显示图形
        plt.tight_layout()
        plt.show()


        # 绘制Cdl散点图和拟合直线
        # 确定有多少不同的组
        num_groups = summary_df['Group'].nunique()

        # 准备绘图
        fig, ax_scatter = plt.subplots(figsize=(8, 6))
        colors = plt.cm.Paired(np.linspace(0, 1, num_groups))

        # 为每个组绘制散点图和拟合直线
        for i in range(num_groups):
            group_df = summary_df[summary_df['Group'] == i]
            scan_rates = group_df['Scan Rate (mV/s)']
            current_diffs = group_df['Current Density Difference (mA/cm²)']
            label = group_df['structure'].iloc[0]
            ax_scatter.scatter(scan_rates, current_diffs, color=colors[i], label=label)

            # 执行线性拟合
            if len(scan_rates) > 1:  # 需要至少两点才能进行拟合
                slope, intercept = np.polyfit(scan_rates, current_diffs, 1)
                ax_scatter.plot(scan_rates, slope * scan_rates + intercept, color=colors[i], linestyle='--', label=f'Fit line (Slope $C_{{dl}}$ = {slope*1000:.2f} $mF/cm^2$)')
                ax_scatter.set_xlabel("Scan Rate (mV/s)")
                ax_scatter.set_ylabel("Current Density Difference (mA/cm²)")
                ax_scatter.legend(loc='best', frameon=False, shadow=False)
                plt.tight_layout()  # 自动调整子图参数，使之填充整个图像区域。
                plt.show()

        self.summary_df = summary_df

    def saveData_Cdl(self):
        if not self.data_Cdl:
            QMessageBox.warning(self, "警告", "没有数据可保存！")
            return

        # 询问用户保存文件的位置
        save_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "data_Cdl", "Excel Files (*.xlsx)")
        if not save_path:
            return  # 用户取消了保存

        # 使用 plainTextEdit_Cdl_Label 中的每行内容作为标签
        sample_text = self.plainTextEdit_Cdl_Label.toPlainText().split("\n")

        # 创建一个Pandas ExcelWriter对象
        with pd.ExcelWriter(save_path) as writer:
            for sample, data in zip(sample_text, self.list_Cdl_data):
                # 将数据写入Excel文件的对应sheet
                data.to_excel(writer, sheet_name=sample, index=False)
            self.summary_df_Cdl.to_excel(writer, sheet_name='summary')

        QMessageBox.information(self, "保存数据", "Cdl数据已成功保存！")
############################# Cdl模块：结束 #############################

############################# Tafel模块：开始 #############################
    # Tafel 数据添加方法
    def addData_Tafel(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Excel Files", "", "Excel Files (*.xlsx *.xls)")
        if files:
            self.fileNames_Tafel.extend(files)
            # 更新 UI 以显示选择的文件
            current_text = self.plainTextEdit_Tafel_Data.toPlainText()
            new_text = "\n".join(files) if not current_text else current_text + "\n" + "\n".join(files)
            self.plainTextEdit_Tafel_Data.setPlainText(new_text)

            # 将每组数据的父文件夹名保存在 plainTextEdit_Tafel_Label 中
            for file in files:
                folder_name = os.path.basename(os.path.dirname(file))  # 获取父文件夹名
                current_label_text = self.plainTextEdit_Tafel_Label.toPlainText()
                new_label_text = folder_name if not current_label_text else current_label_text + "\n" + folder_name
                self.plainTextEdit_Tafel_Label.setPlainText(new_label_text)

            # 调整文本框高度以显示所有内容
            self.adjustPlainTextEditHeight(self.plainTextEdit_Tafel_Data)
            self.adjustPlainTextEditHeight(self.plainTextEdit_Tafel_Label)

    # Tafel 数据导入方法
    def importData_Tafel(self):
        if self.isDataImported_Tafel:  # 如果数据已导入，则清除数据
            self.clearData_Tafel()
            return
        
        if not self.fileNames_Tafel:  # 检查是否已添加文件
            QMessageBox.warning(self, "警告", "请先添加文件！")
            return
        
        for file in self.fileNames_Tafel:
            data = pd.read_excel(file, index_col=None, header=0)
            self.data_Tafel.append(data)

            # 获取父文件夹名称
            parent_folder_name = os.path.basename(os.path.dirname(file))

            # 在 frame_TafelSlope 中动态添加 Label 和文本框
            h_layout = QHBoxLayout()

            # 在 frame_TafelSlope 中动态添加 Label 和文本框
            label = QLabel(parent_folder_name)
            line_edit_max = QLineEdit("0")
            line_edit_row_count = QLineEdit(str(data.shape[0]))

            # 将 Label 和 line_edit 添加到水平布局中
            h_layout.addWidget(label)
            h_layout.addWidget(line_edit_max)
            h_layout.addWidget(line_edit_row_count)

            # 将水平布局添加到 frame_TafelSlope 的垂直布局中
            self.frame_TafelSlope.layout().addLayout(h_layout)

        # 数据导入后显示弹窗提醒
        QMessageBox.information(self, "导入数据", "Tafel 数据已成功导入！")

        # 数据导入成功后
        self.isDataImported_Tafel = True
        self.btn_importData_Tafel.setText("清除数据")

    def clearData_Tafel(self):
        # 清除存储的数据和文件名
        self.data_Tafel.clear()
        self.fileNames_Tafel.clear()

        # 清空文本框
        self.plainTextEdit_Tafel_Data.setPlainText("")
        self.plainTextEdit_Tafel_Label.setPlainText("")

        # 设置文本框的默认高度
        self.adjustPlainTextEditHeight(self.plainTextEdit_Tafel_Data, minHeight=72)
        self.adjustPlainTextEditHeight(self.plainTextEdit_Tafel_Label, minHeight=72)

        # 移除 frame_TafelSlope 中的所有控件
        layout = self.frame_TafelSlope.layout()
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                # 如果是布局，则递归删除其内的控件
                while item.layout().count():
                    sub_item = item.layout().takeAt(0)
                    sub_widget = sub_item.widget()
                    if sub_widget is not None:
                        sub_widget.deleteLater()

        # 恢复按钮文字并重置状态标志
        self.btn_importData_Tafel.setText("导入数据")
        self.isDataImported_Tafel = False

    # Tafel 绘图方法
    def plotData_Tafel(self):
        if not self.data_Tafel:
            QMessageBox.warning(self, "警告", "请先导入数据！")
            return

        # 使用 plainTextEdit_Tafel_Label 中的每行内容作为标签
        label_text = self.plainTextEdit_Tafel_Label.toPlainText().split("\n")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # 创建左右两个子图
        for i, (label, data) in enumerate(zip(label_text, self.data_Tafel)):
            # 转换数据
            data['Current Density (mA/cm²)'] = data['WE(1).Current (A)'] / self.electrode_area * 1000
            data['Log Current Density'] = np.log10(np.abs(data['Current Density (mA/cm²)']))
            data['Overpotential (V)'] = data['WE(1).Potential (V)'] + self.potential_shift - 1.23

            # 绘制左边的子图
            ax1.plot(data['Log Current Density'], data['Overpotential (V)'], label=label)

            # 获取每个文件对应的两个 lineEdit 中的数值
            start_row = int(self.frame_TafelSlope.layout().itemAt(i).layout().itemAt(1).widget().text())
            end_row = int(self.frame_TafelSlope.layout().itemAt(i).layout().itemAt(2).widget().text())

            # 确保索引在数据范围内
            start_row = max(min(start_row, len(data) - 1), 0)
            end_row = max(min(end_row, len(data) - 1), start_row)

            # 在左边的子图中标记 start_row 和 end_row
            ax1.scatter(data['Log Current Density'][start_row], data['Overpotential (V)'][start_row], color='red', zorder=5)
            ax1.scatter(data['Log Current Density'][end_row], data['Overpotential (V)'][end_row], color='green', zorder=5)

            # 在右边的子图中绘制散点图
            selected_data = data.iloc[start_row:end_row + 1]  # 获取选定的数据范围
            ax2.scatter(selected_data['Log Current Density'], selected_data['Overpotential (V)'], label=label)

            # 线性回归分析并绘制拟合直线
            slope, intercept = np.polyfit(selected_data['Log Current Density'], selected_data['Overpotential (V)'], 1)
            ax2.plot(selected_data['Log Current Density'], slope * selected_data['Log Current Density'] + intercept, label=f'Fit: Tafel slope : {slope*1000:.2f} mV dec$^{{-1}}$')

            # 打印斜率
            print(f"Slope for {label} from {start_row} to {end_row}: {slope:.2f} mV/dec")

        # 设置两个子图的标签和图例
        ax1.set_xlabel('Log j (mA/cm²)')
        ax1.set_ylabel('Overpotential (V)')
        ax1.legend(loc='best', frameon=False, shadow=False)

        ax2.set_xlabel('Log j (mA/cm²)')
        ax2.set_ylabel('Overpotential (V)')
        ax2.legend(loc='best', frameon=False, shadow=False)

        plt.tight_layout()
        plt.show()

    def saveData_Tafel(self):
        # 检查是否已导入数据
        if not self.data_Tafel:
            QMessageBox.warning(self, "警告", "没有数据可保存！")
            return

        # 询问用户保存文件的位置
        save_path, _ = QFileDialog.getSaveFileName(self, "保存文件", "data_Tafel", "Excel Files (*.xlsx)")
        if not save_path:
            return  # 用户取消了保存

        with pd.ExcelWriter(save_path) as writer:
            for i, (file, data) in enumerate(zip(self.fileNames_Tafel, self.data_Tafel)):
                # 转换数据
                data['Current Density (mA/cm²)'] = data['WE(1).Current (A)'] / self.electrode_area * 1000
                data['Log Current Density'] = np.log10(np.abs(data['Current Density (mA/cm²)']))
                data['Overpotential (V)'] = data['WE(1).Potential (V)'] + self.potential_shift - 1.23

                # 获取每个文件对应的两个 lineEdit 中的数值
                start_row = int(self.frame_TafelSlope.layout().itemAt(i).layout().itemAt(1).widget().text())
                end_row = int(self.frame_TafelSlope.layout().itemAt(i).layout().itemAt(2).widget().text())

                # 确保索引在数据范围内
                start_row = max(min(start_row, len(data) - 1), 0)
                end_row = max(min(end_row, len(data) - 1), start_row)

                # 获取用于绘图的数据范围
                selected_data = data.iloc[start_row:end_row + 1][['Log Current Density', 'Overpotential (V)']]

                # 保存整个数据集
                # sheet_name = os.path.splitext(os.path.basename(file))[0]
                sheet_name = os.path.basename(os.path.dirname(file))
                data[['Log Current Density', 'Overpotential (V)']].to_excel(writer, sheet_name=sheet_name, index=False)

                # 保存选定的数据范围
                selected_sheet_name = f"{sheet_name}_{start_row}_{end_row}"
                selected_data.to_excel(writer, sheet_name=selected_sheet_name, index=False)

        QMessageBox.information(self, "保存数据", "Tafel 数据已成功保存！")
############################# Tafel模块：结束 #############################

class NoCloseMDISubWindow(QMdiSubWindow):
    def closeEvent(self, event):
        # 忽略关闭事件
        event.ignore()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # 创建 FunctionWindow 子窗口
        self.function_window = FunctionWindow()
        subWindow = NoCloseMDISubWindow()  # 使用自定义的 NoCloseMDISubWindow 类
        subWindow.setWidget(self.function_window)
        self.mdiArea.addSubWindow(subWindow)
        subWindow.show()

        # 连接菜单栏信号
        self.action_About.triggered.connect(self.on_actionAbout_triggered)
    
    def on_actionAbout_triggered(self):
        # 创建并显示弹窗
        QMessageBox.information(self, "关于", "关于这个程序的一切，\n我可以说一无所知。")

# 主函数
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("images/images/DataPilot_icon.png"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())