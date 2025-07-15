import gradio as gr
import pandas as pd
import numpy as np
from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import roc_curve, auc
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

# ---------------------- LOAD DATA ----------------------
def load_text_data():
    return pd.read_csv('Education.csv')

def load_drug_data():
    return pd.read_csv('drug200.csv')

text_data = load_text_data()
drug_data = load_drug_data()

# ---------------------- TRAIN TEXT MODEL ----------------------
def split_train_test(data, ratio_test=0.2):
    np.random.seed(0)
    index_permu = np.random.permutation(len(data))
    data_permu = data.iloc[index_permu]
    test_size = int(len(data_permu) * ratio_test)
    train_set = data_permu.iloc[:-test_size]
    test_set = data_permu.iloc[-test_size:]
    return train_set.reset_index(drop=True), test_set.reset_index(drop=True)

def train_text_model():
    train_set, test_set = split_train_test(text_data, 0.2)
    X_train, y_train = train_set['Text'], train_set['Label']
    y_train_bin = y_train.map({"positive": 1, "negative": 0})
    count_vect = CountVectorizer(binary=True, stop_words='english')
    X_train_vect = count_vect.fit_transform(X_train)
    model = BernoulliNB()
    model.fit(X_train_vect, y_train_bin)

    X_test, y_test = test_set['Text'], test_set['Label'].map({"positive": 1, "negative": 0})
    X_test_vect = count_vect.transform(X_test)
    y_score = model.predict_proba(X_test_vect)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_score)
    roc_auc = auc(fpr, tpr)

    return model, count_vect, (fpr, tpr, roc_auc)

text_model, vectorizer, roc_data = train_text_model()

# ---------------------- TRAIN DRUG MODEL ----------------------
def train_drug_model():
    df = drug_data.copy()
    label_encoders = {}
    for col in ['Sex', 'BP', 'Cholesterol']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    X = df[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']]
    y = df['Drug']
    model = GaussianNB()
    model.fit(X, y)
    return model, label_encoders

drug_model, encoders = train_drug_model()

# ---------------------- TEXT PREDICTION ----------------------
def predict_sentiment(text):
    if not text.strip():
        return "Vui lòng nhập nội dung văn bản.", None, None

    X_input = vectorizer.transform([text])
    pred_label = text_model.predict(X_input)[0]
    pred_proba = text_model.predict_proba(X_input)[0]

    label_text = "POSITIVE" if pred_label == 1 else "NEGATIVE"
    confidence = round(pred_proba[pred_label] * 100, 2)
    result = f"### Kết quả: `{label_text}`\n### Độ tin cậy: `{confidence}%`"

    fpr, tpr, roc_auc = roc_data
    fig1, ax1 = plt.subplots(figsize=(5, 4))
    ax1.plot(fpr, tpr, color='green', lw=2, label=f'AUC = {roc_auc:.2f}')
    ax1.plot([0, 1], [0, 1], color='gray', lw=1, linestyle='--')
    ax1.set_xlim([0.0, 1.0])
    ax1.set_ylim([0.0, 1.05])
    ax1.set_xlabel('False Positive Rate')
    ax1.set_ylabel('True Positive Rate')
    ax1.set_title('Đường cong ROC')
    ax1.legend(loc="lower right")
    buf1 = BytesIO()
    plt.tight_layout()
    plt.savefig(buf1, format="png")
    plt.close()
    buf1.seek(0)
    img1 = Image.open(buf1)

    fig2, ax2 = plt.subplots()
    ax2.bar(['Negative', 'Positive'], pred_proba, color=['red', 'green'], alpha=0.7)
    ax2.set_title('Xác suất dự đoán cho văn bản')
    ax2.set_ylabel('Độ tin cậy')
    for i, v in enumerate(pred_proba):
        ax2.text(i, v + 0.02, f"{v:.2f}", ha='center', va='bottom', fontweight='bold')
    buf2 = BytesIO()
    plt.tight_layout()
    plt.savefig(buf2, format="png")
    plt.close()
    buf2.seek(0)
    img2 = Image.open(buf2)

    return result, img1, img2

# ---------------------- DRUG PREDICTION ----------------------
def predict_drug(age, sex, bp, cholesterol, na_to_k):
    try:
        sex_enc = encoders['Sex'].transform([sex])[0]
        bp_enc = encoders['BP'].transform([bp])[0]
        chol_enc = encoders['Cholesterol'].transform([cholesterol])[0]

        X_input = np.array([[age, sex_enc, bp_enc, chol_enc, na_to_k]])
        pred = drug_model.predict(X_input)[0]
        proba = drug_model.predict_proba(X_input)[0]

        # Bar chart
        fig, ax = plt.subplots()
        classes = drug_model.classes_
        ax.bar(classes, proba, color='skyblue')
        ax.set_title("Xác suất dự đoán các loại thuốc")
        ax.set_ylabel("Xác suất")
        for i, v in enumerate(proba):
            ax.text(i, v + 0.01, f"{v:.2f}", ha='center', va='bottom')
        buf = BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format="png")
        plt.close()
        buf.seek(0)
        img = Image.open(buf)

        return f"### Loại thuốc phù hợp: `{pred}`", img

    except Exception as e:
        return f"Lỗi: {e}", None

# ---------------------- GRADIO INTERFACES ----------------------

# Văn bản giáo dục
iface1 = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=5, label="Nhập văn bản cần phân loại"),
    outputs=[
        gr.Markdown(label="Kết quả dự đoán"),
        gr.Image(label="Biểu đồ ROC"),
        gr.Image(label="Biểu đồ xác suất văn bản")
    ],
    title="🎓 Phân loại văn bản Giáo dục",
    description="Sử dụng Bernoulli Naive Bayes để phân loại cảm xúc (positive/negative) từ văn bản.",
    theme="soft"
)

# Dự đoán thuốc
iface2 = gr.Interface(
    fn=predict_drug,
    inputs=[
        gr.Slider(15, 80, step=1, label="Tuổi bệnh nhân"),
        gr.Radio(['F', 'M'], label="Giới tính"),
        gr.Radio(['LOW', 'NORMAL', 'HIGH'], label="Huyết áp"),
        gr.Radio(['NORMAL', 'HIGH'], label="Cholesterol"),
        gr.Number(label="Tỷ lệ Na/K trong máu")
    ],
    outputs=[
        gr.Markdown(label="Kết quả dự đoán thuốc"),
        gr.Image(label="Biểu đồ xác suất thuốc")
    ],
    title="💉 Dự đoán loại thuốc phù hợp",
    description="Sử dụng Gaussian Naive Bayes để dự đoán thuốc phù hợp từ thông tin y tế.",
    theme="soft"
)

# Giao diện chung với Tab
demo = gr.TabbedInterface(
    [iface1, iface2],
    ["Phân loại Văn bản", "Dự đoán Thuốc"]
)

demo.launch(share=False)
