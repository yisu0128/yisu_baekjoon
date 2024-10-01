def solution(phone_book):
    answer = True
    phone_book_dict = [phone1 for phone1, phone2 in phone_book]
    if phone_book_dict.keys() != phone_book_dict.values():
        if phone1[0:len(phone1)] == phone2[0:len(phone2)]:
            answer= false
    return answer
