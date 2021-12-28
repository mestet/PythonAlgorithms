# Вводится карта проходимых в обе стороны тоннелей подземлья в виде строк,
# содержащих разделённые пробелом названия двух пещер, которые соединяет соответствующий тоннель.
# Две последние строки не содержат пробелов — это название входа в подземелье и название выхода.
# Вывести "YES", если из входа можно попасть в выход, и "NO" в противном случае.
# Пары могут повторяться или содержать одинаковые слова


def dungeon_map():
    raw_in = input()
    dungeon = dict()
    while " " in raw_in:
        l_room, r_room = raw_in.split()
        merge_dungeon(dungeon, r_room, l_room)
        merge_dungeon(dungeon, l_room, r_room)
        raw_in = input()
    d_start = raw_in
    d_exit = input()

    reachable = dungeon.get(d_start)
    while True:
        new_reachable = set()
        for room in reachable:
            new_reachable |= dungeon.get(room)
        if new_reachable.issubset(reachable):
            break
        else:
            reachable |= new_reachable

    if d_exit in reachable:
        return "YES"
    return "NO"


def merge_dungeon(dun, room, neighbour):
    if room in dun:
        dun[room] |= {neighbour}
    else:
        dun |= {room: {neighbour}}


if __name__ == "__main__":
    print(dungeon_map())
