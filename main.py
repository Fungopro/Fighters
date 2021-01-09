from Fighter.Fighter import Fighter

if __name__ == '__main__':
    fighter1 = Fighter('guard_1')
    fighter2 = Fighter('guard_2')
    fighter3 = Fighter('guard_3')
    arr = [fighter1, fighter2, fighter3]
    while True:
        if 'fighter1' in locals() and len(arr) > 1:
            fighter1.random_attack(arr)
            if fighter1.hp <= 0:
                arr.remove(fighter1)
                del fighter1
        if 'fighter2' in locals() and len(arr) > 1:
            fighter2.random_attack(arr)
            if fighter2.hp <= 0:
                arr.remove(fighter2)
                del fighter2
        if 'fighter3' in locals() and len(arr) > 1:
            fighter3.random_attack(arr)
            if fighter3.hp <= 0:
                arr.remove(fighter3)
                del fighter3
        for item in arr:
            if item is not None:
                item.get_info()
        if len(arr) == 1:
            print(arr[0], 'is winner!')
            break

