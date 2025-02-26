import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = {
    "ก": "กอ ไก่",
    "ข": "ขอ ไข่",
    "ค": "คอ ควาย",
    "ง": "งอ งู",
    "จ": "จอ จาน",
    "ฉ": "ฉอ ฉิ่ง",
    "ช": "ชอ ช้าง",
    "ซ": "ซอ โซ่",
    "ญ": "ญอ หญิง",
    "ฎ": "ฎอ ชฎา",
    "ฏ": "ฏอ ปฏัก",
    "ฐ": "ฐอ ฐาน",
    "ฑ": "ฑอ มณโฑ",
    "ณ": "ณอ เณร",
    "ด": "ดอ เด็ก",
    "ต": "ตอ เต่า",
    "ถ": "ถอ ถุง",
    "ท": "ทอ ทหาร",
    "น": "นอ หนู",
    "บ": "บอ ใบไม้",
    "ป": "ปอ ปลา",
    "ผ": "ผอ ผึ้ง",
    "ฝ": "ฝอ ฝา",
    "พ": "พอ พาน",
    "ฟ": "ฟอ ฟัน",
    "ม": "มอ ม้า",
    "ย": "ยอ ยักษ์",
    "ร": "รอ เรือ",
    "ล": "ลอ ลิง",
    "ว": "วอ แหวน",
    "ศ": "ศอ ศาลา",
    "ษ": "ษอ ฤๅษี",
    "ส": "สอ เสือ",
    "ห": "หอ หีบ",
    "อ": "ออ อ่าง",
    "ฮ": "ฮอ นกฮูก"
}

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        
        self.current_consonant = None
        self.is_flipped = False
        
        self.card = tk.Label(root, text="", font=("Arial", 60), width=10, height=5, relief="ridge", borderwidth=3, bg="white")
        self.card.pack(pady=50)
        self.card.bind("<Button-1>", self.flip_card)
        
        self.next_button = tk.Button(root, text="Next", font=("Arial", 20), command=self.next_card)
        self.next_button.pack()
        
        self.next_card()
    
    def next_card(self):
        self.current_consonant = random.choice(list(thai_consonants.keys()))
        self.card.config(text=self.current_consonant, bg="white")
        self.is_flipped = False
    
    def flip_card(self, event):
        if not self.is_flipped:
            self.card.config(text=thai_consonants[self.current_consonant], bg="lightgray")
            self.is_flipped = True
        else:
            self.card.config(text=self.current_consonant, bg="white")
            self.is_flipped = False

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
