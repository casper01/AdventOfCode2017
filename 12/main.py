"""
Day 12: Digital Plumber
"""

NO_GID = -1


def get_group(neighbours_dict, program_id, found_programs):
    found_programs.append(program_id)
    neighbours = neighbours_dict[program_id]

    for neighbour in neighbours:
        if neighbour not in found_programs:
            found_programs = get_group(
                neighbours_dict, neighbour, found_programs)
    return found_programs


def main():
    data = open('input.txt', 'r')
    pipes = data.readlines()
    neighbours_dict = {}
    gids = {}

    for pipe in pipes:
        main_id = int(pipe.split('<->')[0])
        neighbours = pipe.split('<->')[1].split(',')
        neighbours = list(map(int, neighbours))
        neighbours_dict[main_id] = neighbours
        gids[main_id] = NO_GID

    zero_group = get_group(neighbours_dict, 0, [])
    print('len of zero group:', len(zero_group))

    groups = 0
    for program_id in neighbours_dict:
        if gids[program_id] != NO_GID:
            continue
        groups += 1
        group = get_group(neighbours_dict, program_id, [])
        for program in group:
            gids[program] = groups
    print('unique groups:', groups)


if __name__ == '__main__':
    main()
