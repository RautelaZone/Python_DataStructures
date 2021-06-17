def main():
    print("Enter number of test cases: ")
    test_cases = int(input())
    count = 0
    result = []

    while test_cases > 0:
        print("Enter number of players:")
        no_of_players = int(input())

        villian = [int(x) for x in input().strip().split()]
        player = [int(x) for x in input().strip().split()]

        villian.sort(reverse=True)
        player.sort(reverse=True)

        start = 0

        for i in range(no_of_players):
            for j in range(start, no_of_players):
                if player[i] > villian[j]:
                    start = j + 1
                    count += 1
                    break

        if count == no_of_players:
            result.append("WIN")
            test_cases -= 1
        else:
            result.append("LOSE")
            test_cases -= 1
        count = 0

    for final_result in result:
        print(final_result)


main()
