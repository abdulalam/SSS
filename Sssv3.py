import pandas as pd
import xlsxwriter

df = pd.read_csv('data.csv')
shelf_list_with_stock = []
for row in df["Shelf No."]:
    if row[-1] != "z":
        shelf_list_with_stock.append(row)
# print(shelf_list_with_stock)
# print(len(shelf_list_with_stock))

print(f"First isle num :--> {shelf_list_with_stock[0][0:3]}")
print(f"Last isle num:--> {int(shelf_list_with_stock[-1][0:3])}")

use_default = input("Use default Y/N--> ").upper()
if use_default == "Y":
    islenum_start = int(shelf_list_with_stock[0][0:3])
    islenum_end = int(shelf_list_with_stock[-1][0:3]) + 1

    # bay height a-t 0 to 6
    input_height_start = "B"
    input_height_end = "G"
else:

    # start and end isle num
    islenum_start = int(input("Start isle num e.g 501--> "))
    islenum_end = int(input("End isle num e.g 598--> ")) + 1

    # bay height a-t 0 to 6
    input_height_start = input("START level (A-G) --> ").upper()
    input_height_end = input("END level (A-G) --> ").upper()

# creating full_shelf_list

long_isles = [501, 504, 505, 508, 509, 512, 513, 516, 517, 520, 521, 524, 525, 528, 529, 532, 533, 536, 537, 540, 541,
              564, 565, 568, 569, 572, 573, 576, 577, 580, 581, 584, 585, 588, 589, 592, 593, 596, 597, 608]
bay_height = ["A", "B", "C", "D", "E", "F", "G"]
#tunnel = ["43B", "43C", "44B", "44C", "45B", "45C"]
tunnel = ["123"]



# short isles
short_Bay_Range_1 = 4
short_Bay_Range_2 = 10
short_Bay_Range_3 = 10
short_Bay_Range_4 = 82

short_Bay_User_input_start = int(input("Short bay start e.g 4 > "))
short_Bay_User_input_end = int(input("Short bay End e.g 81 > ")) + 1


if short_Bay_User_input_start <= 9 and short_Bay_User_input_end <= 9:
    short_Bay_Range_1 = short_Bay_User_input_start
    short_Bay_Range_2 = short_Bay_User_input_end
    short_Bay_Range_3 = 0
    short_Bay_Range_4 = 0
elif short_Bay_User_input_start <= 9 and short_Bay_User_input_end >= 9:
    short_Bay_Range_1 = short_Bay_User_input_start
    short_Bay_Range_2 = 10
    short_Bay_Range_3 = 10
    short_Bay_Range_4 = short_Bay_User_input_end
elif short_Bay_User_input_start >= 9 and short_Bay_User_input_end >= 9:
    short_Bay_Range_1 = 0
    short_Bay_Range_2 = 0
    short_Bay_Range_3 = short_Bay_User_input_start
    short_Bay_Range_4 = short_Bay_User_input_end


# long isle
long_Bay_Range_1 = 4
long_Bay_Range_2 = 10
long_Bay_Range_3 = 10
long_Bay_Range_4 = 85

long_Bay_User_input_start = int(input("long bay Start e.g 4 > "))
long_Bay_User_input_end = int(input("long bay End e.g 84 > ")) + 1


if long_Bay_User_input_start <= 9 and long_Bay_User_input_end <= 9:
    long_Bay_Range_1 = long_Bay_User_input_start
    long_Bay_Range_2 = long_Bay_User_input_end
    long_Bay_Range_3 = 0
    long_Bay_Range_4 = 0
elif long_Bay_User_input_start <= 9 and long_Bay_User_input_end >= 9:
    long_Bay_Range_1 = long_Bay_User_input_start
    long_Bay_Range_2 = 10
    long_Bay_Range_3 = 10
    long_Bay_Range_4 = long_Bay_User_input_end
elif long_Bay_User_input_start >= 9 and long_Bay_User_input_end >= 9:
    long_Bay_Range_1 = 0
    long_Bay_Range_2 = 0
    long_Bay_Range_3 = long_Bay_User_input_start
    long_Bay_Range_4 = long_Bay_User_input_end



full_shelf_list = []
for select_isle_num in range(islenum_start, islenum_end):
    if select_isle_num not in range(599, 608) and select_isle_num not in range(542, 563):
        if select_isle_num in long_isles:

            for bay in range(long_Bay_Range_1, long_Bay_Range_2):
                for select_bay_height in bay_height[
                                         bay_height.index(input_height_start):bay_height.index(input_height_end) + 1]:
                    full_shelf_list.append(f"{select_isle_num}-00{bay}{select_bay_height}")
            for bay in range(long_Bay_Range_3, long_Bay_Range_4):
                for select_bay_height in bay_height[
                                         bay_height.index(input_height_start):bay_height.index(input_height_end) + 1]:
                    if f"{bay}{select_bay_height}" not in tunnel:
                        full_shelf_list.append(f"{select_isle_num}-0{bay}{select_bay_height}")

        else:

            for bay in range(short_Bay_Range_1, short_Bay_Range_2):
                for select_bay_height in bay_height[
                                         bay_height.index(input_height_start):bay_height.index(input_height_end) + 1]:
                    full_shelf_list.append(f"{select_isle_num}-00{bay}{select_bay_height}")
            for bay in range(short_Bay_Range_3, short_Bay_Range_4):
                for select_bay_height in bay_height[
                                         bay_height.index(input_height_start):bay_height.index(input_height_end) + 1]:
                    if f"{bay}{select_bay_height}" not in tunnel:
                        full_shelf_list.append(f"{select_isle_num}-0{bay}{select_bay_height}")

cleaning_for_000_bays_list_temp = []
for cleaning_bay_temp in full_shelf_list:

    if cleaning_bay_temp[4:7] == "000":
        cleaning_for_000_bays_list_temp.append(cleaning_bay_temp)
for deleteing_000_bays in cleaning_for_000_bays_list_temp:
    full_shelf_list.remove(deleteing_000_bays)







combined_list = full_shelf_list + shelf_list_with_stock
empty_locations = []
# print(combined_list)
current_progress = 0
for locations in full_shelf_list:
    progress = round((full_shelf_list.index(locations) / len(full_shelf_list)) * 10)

    if current_progress < progress:
        print(f"{current_progress * 10}-", end="", flush=True)
        current_progress = progress

    if locations not in shelf_list_with_stock:
        empty_locations.append(locations)

print("100")
print(f'Total = {len(empty_locations)}/{len(full_shelf_list)}')
print(f"Total = {round((len(empty_locations) / len(full_shelf_list)) * 100, 1)}%")

stats = []
stats_temp_holder = []

total_empty_percentage = round((len(empty_locations) / len(full_shelf_list)) * 100, 2)
stats.append("Empty")
stats.append(f"{total_empty_percentage}%")
for islenum in range(islenum_start, islenum_end):

    if islenum not in range(599, 608):

        for select_empty_locations in empty_locations:

            if select_empty_locations[0:3] == str(islenum):
                stats_temp_holder.append(select_empty_locations)

        stats.append(islenum)
        stats.append(len(stats_temp_holder))
        stats_temp_holder.clear()

# filter empty_locations

a_height_locations = []
b_height_locations = []
c_height_locations = []
d_height_locations = []
e_height_locations = []
f_height_locations = []
g_height_locations = []
temp_location_holder = []

for select_empty_locations in empty_locations:
    if select_empty_locations[-1] == "G":
        g_height_locations.append(select_empty_locations)

    elif select_empty_locations[-1] == "A":
        a_height_locations.append(select_empty_locations)
    elif select_empty_locations[-1] == "B":
        b_height_locations.append(select_empty_locations)
    elif select_empty_locations[-1] == "C":
        c_height_locations.append(select_empty_locations)
    elif select_empty_locations[-1] == "D":
        d_height_locations.append(select_empty_locations)
    elif select_empty_locations[-1] == "E":
        e_height_locations.append(select_empty_locations)
    elif select_empty_locations[-1] == "F":
        f_height_locations.append(select_empty_locations)

print(f'A = {len(a_height_locations)}')
print(f'B = {len(b_height_locations)}')
print(f'C = {len(c_height_locations)}')
print(f'D = {len(d_height_locations)}')
print(f'E = {len(e_height_locations)}')
print(f'F = {len(f_height_locations)}')
print(f'G = {len(g_height_locations)}')

filter = True

while filter:
    user_filter_input = input("-->").upper()

    if user_filter_input == "A":
        print(a_height_locations)
    elif user_filter_input == "B":
        print(b_height_locations)
    elif user_filter_input == "C":
        print(c_height_locations)
    elif user_filter_input == "D":
        print(d_height_locations)
    elif user_filter_input == "E":
        print(e_height_locations)
    elif user_filter_input == "F":
        print(f_height_locations)
    elif user_filter_input == "G":
        print(g_height_locations)
    elif user_filter_input == "VNA":
        print(
            b_height_locations + c_height_locations + d_height_locations + e_height_locations + f_height_locations + g_height_locations)
    elif user_filter_input == "S":
        print(
            b_height_locations + c_height_locations + d_height_locations + e_height_locations + f_height_locations)

    elif user_filter_input == "EXIT":

        exit()
    elif user_filter_input == "ALL":
        for location in empty_locations:
            print(location)

    elif user_filter_input == "PRINT":
        print("out excel")
        outWorkbook = xlsxwriter.Workbook("print.xlsx")
        outSheet = outWorkbook.add_worksheet()
        outSheet1 = outWorkbook.add_worksheet()
        y = 0
        x = 0
        isle = 501
        for current_num in range(len(empty_locations)):
            current_isle = int(empty_locations[current_num][0:3])

            if current_isle != isle:
                isle = current_isle
                x = 10

            if x >= 9:
                x = 0
                y = y + 1
            outSheet.write(y, x, empty_locations[current_num])
            x = x + 1

        y = 0
        x = 0
        for stat in range(len(stats)):

            if x >= 2:
                x = 0
                y = y + 1
            outSheet1.write(y, x, stats[stat])
            x = x + 1
        outWorkbook.close()

    elif user_filter_input == "STATS":
        for islenum in range(islenum_start, islenum_end):

            if islenum not in range(599, 608):

                for select_empty_locations in empty_locations:

                    if select_empty_locations[0:3] == str(islenum):
                        temp_location_holder.append(select_empty_locations)

                print(f"{islenum} --> {len(temp_location_holder)}")
                temp_location_holder.clear()

    elif user_filter_input == "FILTER":
        y = 1
        while y == 1:
            select_isle = input("Islenum/Exit   ---")
            if select_isle.upper() == "EXIT":
                break
            start_height = input("Start height ->").upper()
            end_height = input("End height  ->").upper()

            select_level = ["A", "B", "C", "D", "E", "F", "G"]
            for select_empty_locations in empty_locations:
                for height in select_level[select_level.index(start_height):select_level.index(end_height) + 1]:

                    if select_empty_locations[0:3] == str(select_isle) and select_empty_locations[-1] == height:
                        temp_location_holder.append(select_empty_locations)

            print(
                f"Number of spaces in {select_isle} at {select_level[select_level.index(start_height):select_level.index(end_height) + 1]} level ---> {len(temp_location_holder)}")
            print(temp_location_holder)
            temp_location_holder.clear()

    else:
        print("Type a, b, c, d, e, f, g, stats, print, all, filter or exit")
