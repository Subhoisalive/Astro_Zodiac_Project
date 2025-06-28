import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Zodiac date ranges
zodiac_signs = [
    ("Capricorn", (12, 22), (1, 19)),
    ("Aquarius", (1, 20), (2, 18)),
    ("Pisces", (2, 19), (3, 20)),
    ("Aries", (3, 21), (4, 19)),
    ("Taurus", (4, 20), (5, 20)),
    ("Gemini", (5, 21), (6, 20)),
    ("Cancer", (6, 21), (7, 22)),
    ("Leo", (7, 23), (8, 22)),
    ("Virgo", (8, 23), (9, 22)),
    ("Libra", (9, 23), (10, 22)),
    ("Scorpio", (10, 23), (11, 21)),
    ("Sagittarius", (11, 22), (12, 21)),
]

# Numerology Data
numerology_data = {
    1: {
        "title": "The Leader",
        "keywords": "Independent, ambitious, original, self-reliant, assertive",
        "strengths": "Leadership qualities, innovation, determination",
        "weaknesses": "Stubbornness, egotism, impatience",
        "career": "Entrepreneur, leader, inventor, CEO",
        "karmic": "You are here to learn self-confidence and leadership. Trust your inner strength and forge your own path, but remember: true power lies in humility and service, not ego."
    },
    2: {
        "title": "The Diplomat",
        "keywords": "Sensitive, cooperative, peacemaker, intuitive, nurturing",
        "strengths": "Harmony, tact, teamwork, empathy",
        "weaknesses": "Over-sensitivity, dependency, indecisiveness",
        "career": "Counselor, mediator, artist, social worker",
        "karmic": "You are here to learn the power of patience, cooperation, and love. Balance your emotions and avoid becoming overly dependent on others. Trust your intuition—it’s your greatest guide."
    },
    3: {
        "title": "The Communicator",
        "keywords": "Creative, expressive, joyful, social, imaginative",
        "strengths": "Optimism, charisma, artistic talent",
        "weaknesses": "Scattered energy, superficiality, exaggeration",
        "career": "Writer, actor, public speaker, artist",
        "karmic": "You are meant to uplift and inspire others through joy, creativity, and expression. Use your voice wisely, and avoid wasting your energy on trivial matters or self-doubt."
    },
    4: {
        "title": "The Builder",
        "keywords": "Practical, disciplined, hardworking, reliable, structured",
        "strengths": "Organization, loyalty, stability, perseverance",
        "weaknesses": "Rigidity, stubbornness, narrow-mindedness",
        "career": "Engineer, manager, accountant, architect",
        "karmic": "You are here to master discipline, order, and stability. Through persistence and honesty, you create strong foundations. Don’t resist structure—embrace it to build your legacy."
    },
    5: {
        "title": "The Adventurer",
        "keywords": "Freedom-loving, curious, energetic, dynamic, versatile",
        "strengths": "Adaptability, enthusiasm, multi-tasking",
        "weaknesses": "Restlessness, impulsiveness, inconsistency",
        "career": "Traveler, salesperson, journalist, marketer",
        "karmic": "Freedom is your soul’s calling, but with freedom comes responsibility. Learn to balance your desire for change with focus and accountability. Don’t run—transform."
    },
    6: {
        "title": "The Nurturer",
        "keywords": "Responsible, loving, caring, protective, compassionate",
        "strengths": "Healing, family-oriented, service-minded",
        "weaknesses": "Overbearing, perfectionist, self-sacrificing",
        "career": "Teacher, doctor, caregiver, community leader",
        "karmic": "You are here to serve, heal, and love unconditionally. But remember: true care begins with the self. Don’t carry others’ burdens to the point of losing your own identity."
    },
    7: {
        "title": "The Seeker",
        "keywords": "Analytical, spiritual, thoughtful, introspective, intellectual",
        "strengths": "Wisdom, intuition, deep thinking",
        "weaknesses": "Isolation, skepticism, detachment",
        "career": "Researcher, scientist, philosopher, mystic",
        "karmic": "You are on a journey of spiritual awakening. Seek knowledge not just with the mind, but with the soul. Let go of skepticism and trust in the divine rhythm of the universe."
    },
    8: {
        "title": "The Powerhouse",
        "keywords": "Ambitious, authoritative, successful, practical, strong-willed",
        "strengths": "Financial acumen, executive skills, discipline",
        "weaknesses": "Workaholism, materialism, dominance",
        "career": "Businessperson, banker, politician, executive",
        "karmic": "You are here to learn the proper use of power, wealth, and authority. Lead with integrity and use your strength to uplift others. The material and spiritual must work hand in hand."
    },
    9: {
        "title": "The Humanitarian",
        "keywords": "Compassionate, generous, idealistic, selfless, artistic",
        "strengths": "Global awareness, emotional depth, forgiveness",
        "weaknesses": "Over-emotional, vulnerable, overly idealistic",
        "career": "Artist, teacher, activist, healer",
        "karmic": "You are an old soul, here to release attachments and serve the world with compassion. Let go of past wounds, forgive freely, and embrace your role as a guide for collective healing."
    }
}


def get_zodiac_sign(day, month):
    for sign, (start_month, start_day), (end_month, end_day) in zodiac_signs:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign
    return "Capricorn"

def calculate_life_path_number(d):
    digits = [int(x) for x in d.strftime("%d%m%Y")]
    while len(digits) > 1:
        digits = [int(x) for x in str(sum(digits))]
    return digits[0]

def process():
    dob_str = dob_entry.get()
    time_str = time_entry.get()
    try:
        dob = datetime.strptime(dob_str, "%d-%m-%Y")
        time = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        messagebox.showerror("Input Error", "Please enter DOB as DD-MM-YYYY and Time as HH:MM")
        return

    zodiac = get_zodiac_sign(dob.day, dob.month)
    life_path = calculate_life_path_number(dob)
    data = numerology_data[life_path]

    output = f"""
🗓️ DOB: {dob.strftime('%d %B %Y')} at {time}
🔮 Zodiac Sign: {zodiac}
🔢 Numerology Number: {life_path} – {data['title']}
📌 Keywords: {data['keywords']}
✅ Strengths: {data['strengths']}
❌ Weaknesses: {data['weaknesses']}
💼 Career Suggestions: {data['career']}

🕉️ Karmic Message:
“{data['karmic']}”
    """

    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, output)


# GUI Layout
root = tk.Tk()
root.title("Zodiac & Numerology Analyzer")
root.geometry("600x600")

tk.Label(root, text="Enter Date of Birth (DD-MM-YYYY):").pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

tk.Label(root, text="Enter Time of Birth (HH:MM 24hr):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Button(root, text="Analyze", command=process, bg="blue", fg="white").pack(pady=10)

result_text = tk.Text(root, wrap=tk.WORD, height=25)
result_text.pack(expand=True, fill=tk.BOTH)

root.mainloop()