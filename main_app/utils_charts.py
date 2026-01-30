# main_app/utils_charts.py
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import numpy as np

def generate_bar_chart(labels, values, title="Biểu đồ", xlabel="", ylabel=""):
    """Tạo biểu đồ cột"""
    plt.figure(figsize=(10, 6))
    colors = plt.cm.Set3(np.arange(len(labels)))
    bars = plt.bar(labels, values, color=colors, edgecolor='black')
    
    # Thêm giá trị trên mỗi cột
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    return save_plot_to_base64()

def generate_pie_chart(labels, values, title="Biểu đồ tròn"):
    """Tạo biểu đồ tròn"""
    plt.figure(figsize=(8, 8))
    colors = plt.cm.Pastel1(np.arange(len(labels)))
    
    # Tạo biểu đồ
    patches, texts, autotexts = plt.pie(
        values, 
        labels=labels, 
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops={'edgecolor': 'black', 'linewidth': 1}
    )
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.axis('equal')
    plt.tight_layout()
    
    return save_plot_to_base64()

def generate_grouped_bar_chart(labels, data1, data2, label1="", label2="", title=""):
    """Tạo biểu đồ cột nhóm"""
    plt.figure(figsize=(12, 6))
    x = np.arange(len(labels))
    width = 0.35
    
    plt.bar(x - width/2, data1, width, label=label1, color='#4CAF50', edgecolor='black')
    plt.bar(x + width/2, data2, width, label=label2, color='#FF5722', edgecolor='black')
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Môn học')
    plt.ylabel('Số lượng')
    plt.xticks(x, labels, rotation=45, ha='right')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    return save_plot_to_base64()

def save_plot_to_base64():
    """Lưu biểu đồ thành base64 string"""
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
    plt.close()  # Quan trọng: đóng figure để giải phóng bộ nhớ
    buf.seek(0)
    
    # Encode base64
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{image_base64}"