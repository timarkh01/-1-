from PIL import Image, ImageDraw
import json


class Bus():
    def __init__(self, seats, access):
        self.seats = seats
        self.access = access
        self.revenue = 0
        self.number = 0
        self.data = []

    def __str__(self):
        ans = ''
        for seat in self.seats:
            ans += f'{seat[0]}\t{seat[1]}\t\t{seat[2]}\t{seat[3]}\n'
        return ans[:-1]
    
    def free_seats(self):
        ans = []
        count = 1
        for seat in self.seats:
            for place in seat:
                if place != 0:
                    ans.append((count, place))
                count += 1
        return ans
    
    def buy_ticket(self, number):
        place = self.seats[(number - 1) // 4][number - ((number - 1) // 4 * 4) - 1]
        if place == 0:
            return f'You cannot buy a ticket for a seat {number}.'
        self.number += 1
        self.revenue += place
        self.seats[(number - 1) // 4][number - ((number - 1) // 4 * 4) - 1] = 0
        line = {}
        line['serial'] = self.number
        line['operation'] = 'buy'
        line['place'] = number
        line['cost'] = place
        self.data.append(line)
        return f'You bought a ticket to a place {number} for {place} RUB.'
    
    def ticket_refund(self, number, cost):
        self.number += 1
        line = {}
        line['serial'] = self.number
        line['operation'] = 'refund'
        line['place'] = number
        line['cost'] = cost
        self.data.append(line)
        self.revenue -= cost
        self.seats[(number - 1) // 4][number - ((number - 1) // 4 * 4) - 1] = cost
        return f'You returned the ticket to the seat {number} and received its cost {cost} RUB.'
    
    def get_report(self, login, pasword):
        with open('report.jsonl', 'w', newline='') as file:
            if login in self.access and self.access[login] == pasword:
                for i in self.data:
                    json.dump(i, file)
                    file.write('\n')
            else:
                json.dump({'error': 'ACCESS DENIED'}, file)

    def set_for_pict(self):
        ans = []
        for seat in self.seats:
            for place in seat:
                if place not in ans:
                    ans.append(place)
        if 0 in ans:
            ans.remove(0)
        return sorted(ans)
    
    def maxim(self):
        ans = 0
        for seat in self.seats:
            for place in seat:
                ans = max(ans, place)
        return ans
    
    def free_places(self):
        ans = []
        for seat in self.seats:
            for place in seat:
                if place == 0:
                    ans.append(place)
        return ans
    
    def __add__(self, other):
        access_ = {}
        for key in self.access:
            if key in other.access:
                access_[key] = other.access[key]
            else:
                access_[key] = self.access[key]
        for key in other.access:
            access_[key] = other.access[key]
        places = []
        free_places = self.free_places() + other.free_places()
        while len(free_places) % 4 != 0:
            free_places.append(max(self.maxim(), other.maxim()))
        line = []
        for i in range(len(free_places)):
            line.append(free_places[i])
            if (i + 1) % 4 == 0:
                places.append(line)
                line = []
        return Bus(places, access_)
    
    def draw_scheme(self, size, name):
        image = Image.new('RGB', (5 * size, len(self.seats) * size), 'white')
        draw = ImageDraw.Draw(image)
        x = 0
        y = 0
        seat_money = self.set_for_pict()
        print(seat_money)
        for seat in self.seats:
            x = 0
            i = 0
            for place in seat:
                if place == 0:
                    color = '#d1dcdd'
                elif place == seat_money[0]:
                    color = '#e2f700'
                elif place == seat_money[1]:
                    color = '#ff92b7'
                elif place == seat_money[2]:
                    color = '#00da72'
                elif place == seat_money[3]:
                    color = '#87a0af'
                else:
                    color = '#2d4942'
                if i == 2:
                    x += size
                draw.rectangle((x, y, x + size, y + size), fill=color, outline='black', width=2)  
                i += 1
                x += size
            y += size
        image.save(name)