import sys


def ops(nums, goal):
    
    if len(nums) == 1:
        return nums[0] == goal
    else:
        return ops([nums[0] + nums[1]] + nums[2:], goal) or \
               ops([nums[0] * nums[1]] + nums[2:], goal)

if __name__ == '__main__':
    with open(sys.argv[1]) as fin:
        total = 0
        for line in fin:
            l, r = line.split(':')
            val = int(l)
            nums = [int(i) for i in r.split()]

            print(val)
            print(nums)
            print()

            if ops(nums,val):
                print("{}: {} = YES".format(val,nums))
                total += val
            else:
                print("{}: {} = NO".format(val,nums))
        
        print(total)

