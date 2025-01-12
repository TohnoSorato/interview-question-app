from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# データベース初期化関数
def init_db():
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            asked_in_interview BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

# 質問リスト
questions_by_category = {
    "new_graduate": [
        "自己紹介をしてください。",
        "学生時代に力を入れたことは何ですか？",
        "この会社を選んだ理由は何ですか？",
        "将来の目標は何ですか？",
        "学業で得た経験をどのように活かせますか？",
        "自分の強みと弱みを教えてください。",
        "当社で実現したいことは何ですか？",
        "ストレスを感じたときの対処法を教えてください。",
        "チームで困難を克服した経験を教えてください。",
        "あなたが最も成長を感じた出来事は何ですか？"
    ],
    "experienced": [
        "これまでのキャリアで最も誇りに思う成果は何ですか？",
        "前職でどのような役割を果たしましたか？",
        "転職を考えた理由を教えてください。",
        "これまでの経験を当社でどのように活かせますか？",
        "リーダーシップを発揮した経験を教えてください。",
        "最も困難だったプロジェクトとその解決方法を教えてください。",
        "顧客との関係構築において重視していることは何ですか？",
        "短期間で成果を出した経験について教えてください。",
        "新しいツールや技術を導入した経験はありますか？",
        "チームのパフォーマンスを向上させた経験を教えてください。"
    ],
    "inexperienced": [
        "未経験の分野に挑戦しようと思った理由は何ですか？",
        "これまでの経験でこの仕事に活かせるスキルは何ですか？",
        "学びたいスキルや目標を教えてください。",
        "新しい業界でどのように成長したいですか？",
        "未経験で困難に直面した場合、どのように対処しますか？",
        "他の分野で得た成功体験を教えてください。",
        "自己啓発のために行ったことを教えてください。",
        "過去に挑戦した最も大きな変化は何ですか？",
        "学びながら成果を出した経験を教えてください。",
        "未経験の環境でどのように価値を提供できますか？"
    ]
}

# 質問取得関数
def get_random_questions(category, mode):
    question_list = questions_by_category.get(category, [])
    total_questions = 10 if mode == "test" else 5
    random.shuffle(question_list)
    session["asked_questions"] = question_list[:total_questions]
    session["question_index"] = 0
    session["total_questions"] = total_questions
    session["mode"] = mode

# データベース操作関数
def save_answer_to_db(question, answer):
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO history (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

def fetch_history_from_db():
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, question, answer, asked_in_interview FROM history")
    data = cursor.fetchall()
    conn.close()
    return data

def delete_history_from_db():
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()

def delete_one_from_db(question):
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history WHERE question = ?", (question,))
    conn.commit()
    conn.close()

def mark_question_as_asked_in_db(question):
    conn = sqlite3.connect("interview.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE history SET asked_in_interview = 1 WHERE question = ?", (question,))
    conn.commit()
    conn.close()

# ルート
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/draw_lot", methods=["POST"])
def draw_lot():
    category = request.form.get("question_type")
    mode = request.form.get("mode")

    if not category or not mode:
        return render_template("index.html", error="カテゴリとモードを選択してください！")

    session["title"] = "テスト用質問" if mode == "test" else "練習用質問"
    get_random_questions(category, mode)
    return redirect(url_for("interview"))

@app.route("/interview", methods=["GET", "POST"])
def interview():
    questions_list = session.get("asked_questions", [])
    question_index = session.get("question_index", 0)
    total_questions = session.get("total_questions", 0)

    if question_index >= total_questions:
        return redirect(url_for("finish"))

    question = questions_list[question_index]
    progress = f"{question_index + 1} / {total_questions}"
    mode = session.get("mode")

    if request.method == "POST":
        if "skip" in request.form:  # スキップボタンが押された場合
            session["question_index"] += 1
            return redirect(url_for("interview"))

        answer = request.form.get("answer", "").strip()
        if mode == "practice" and not answer:
            error = "回答が未入力です。回答を入力するか、スキップしてください。"
            return render_template("interview.html", question=question, progress=progress, title=session.get("title"), mode=mode, error=error)

        session["question_index"] += 1
        save_answer_to_db(question, answer or "未回答")
        return redirect(url_for("interview"))

    return render_template("interview.html", question=question, progress=progress, title=session.get("title"), mode=mode)

@app.route("/history", methods=["GET"])
def history():
    answers = fetch_history_from_db()
    return render_template("history.html", answers=answers)

@app.route("/delete_all", methods=["POST"])
def delete_all():
    delete_history_from_db()
    return redirect(url_for("history"))

@app.route("/delete_one/<question>", methods=["POST"])
def delete_one(question):
    delete_one_from_db(question)
    return redirect(url_for("history"))

@app.route("/mark_as_asked/<question>", methods=["POST"])
def mark_as_asked(question):
    mark_question_as_asked_in_db(question)
    return redirect(url_for("history"))

@app.route("/finish")
def finish():
    return render_template("finish.html")

if __name__ == "__main__":
    init_db()  # アプリ起動時にデータベースを初期化
    app.run(port=5001)
