video_cards_count = int(input('Количество видеокарт: '))
video_cards = []

for card_number in range(1, video_cards_count + 1):
    card_model = int(input(f'Видеокарта {card_number}: '))
    video_cards.append(card_model)

print('Старый список видеокарт:', video_cards)

max_model = max(video_cards)
new_video_cards = []
for card_model in video_cards:
    if card_model != max_model:
        new_video_cards.append(card_model)

print('Новый список видеокарт:', new_video_cards)
