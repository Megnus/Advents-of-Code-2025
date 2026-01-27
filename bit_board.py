def print_bitboard(bb):
    for rank in range(7, -1, -1):
        row = ""
        for file in range(8):
            sq = rank * 8 + file
            row += "1 " if (bb >> sq) & 1 else ". "
        print(row)
    print()


def knight_moves(knight_bb: int) -> int:
    FILE_A  = 0x0101010101010101
    FILE_B  = 0x0202020202020202
    FILE_G  = 0x4040404040404040
    FILE_H  = 0x8080808080808080

    NOT_A   = ~FILE_A & 0xFFFFFFFFFFFFFFFF
    NOT_AB  = ~(FILE_A | FILE_B) & 0xFFFFFFFFFFFFFFFF
    NOT_H   = ~FILE_H & 0xFFFFFFFFFFFFFFFF
    NOT_GH  = ~(FILE_G | FILE_H) & 0xFFFFFFFFFFFFFFFF
    
    moves = 0
    moves |= (knight_bb << 17) & NOT_A
    moves |= (knight_bb << 15) & NOT_H
    moves |= (knight_bb << 10) & NOT_AB
    moves |= (knight_bb << 6)  & NOT_GH

    moves |= (knight_bb >> 17) & NOT_H
    moves |= (knight_bb >> 15) & NOT_A
    moves |= (knight_bb >> 10) & NOT_GH
    moves |= (knight_bb >> 6)  & NOT_AB

    return moves


knight = 1 << (4 + 3 * 8)  # file e=4, rank 4=3 (0-based)
print_bitboard(knight)

knight_moves_bb = knight_moves(knight)
print_bitboard(knight_moves_bb)

KNIGHT_ATTACKS = [0] * 64

for sq in range(64):
    KNIGHT_ATTACKS[sq] = knight_moves(1 << sq)

e4 = 4 + 3 * 8		# file e=4, rank 4=3 (0-based)
d1 = 3 + 0 * 8		# file d=3, rank 1=0 (0-based)
moves_bb = KNIGHT_ATTACKS[d1]


print_bitboard(moves_bb)


def pop_lsb(bb: int):
    lsb = bb & -bb       # isolate lowest set bit
    bb &= bb - 1         # clear that bit
    return lsb, bb


move, moves_bb = pop_lsb(moves_bb)

print_bitboard(move)
print_bitboard(moves_bb)


def bit_to_square(bb: int) -> int:
    return bb.bit_length() - 1


def square_to_bitboard(square_index):
    # square_index should be 0-63
    return 1 << square_index


to_sq = bit_to_square(move)
print(to_sq)

bitboard_bb = square_to_bitboard(to_sq)
print_bitboard(bitboard_bb)


moves = knight_moves(knight)

while moves:
    move, moves = pop_lsb(moves)
    to_sq = move.bit_length() - 1
    print("Knight can move to square:", to_sq)



def coords_to_bitboard(rank, file):
    square_index = (rank * 8) + file
    return 1 << square_index

# Example: 2nd rank (index 1), File C (index 2) -> Square C2


# Display a bitboard with square 18 (C3) set
print_bitboard(1 << 18)


# Rook
# These would be precomputed or provided by a library like 'python-chess'
ROOK_MAGICS = [...] 
ROOK_MASKS = [...] 
ROOK_ATTACK_TABLE = [[...], [...]] # 2D array [square][occupancy_index]

def get_rook_attacks_magic(square, full_occupancy):
    # 1. Mask the occupancy to only relevant squares for this rook
    occ = full_occupancy & ROOK_MASKS[square]
    
    # 2. Apply the "Magic" hashing
    magic_index = (occ * ROOK_MAGICS[square]) >> (64 - rook_relevant_bits[square])
    
    # 3. Direct lookup (O(1) complexity!)
    return ROOK_ATTACK_TABLE[square][magic_index]



def move_piece(rook_bb, from_sq, to_sq):
    # Create a mask for the two squares involved
    move_mask = (1 << from_sq) | (1 << to_sq)
    # XOR toggles the bits: 1 becomes 0 (removal), 0 becomes 1 (placement)
    return rook_bb ^ move_mask

# Example: Move rook from A1 (0) to A5 (32)
white_rooks = 1 << 0
white_rooks = move_piece(white_rooks, 0, 32)



"""
Move Piecebb ^ (1 << from | 1 << to)$O(1)$Check Presencebb & (1 << sq)$O(1)$Generate MovesMagic Bitboard Lookup$O(1)$
"""