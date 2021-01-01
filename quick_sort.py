def quick_sort(nums, left, right):
    pivot = nums[-1]
    if left >= right:
        return
    left_point, right_point = left, right - 1
    while left_point <= right_point:
        print(nums, left_point, right_point)
        while nums[left_point] <= pivot:
            left_point += 1
        while nums[right_point] > pivot:
            right_point -= 1
        if left_point < right_point:
            nums[-1], nums[right_point-1] = nums[right_point-1], nums[-1]
    print(nums)



if __name__ == "__main__":
    nums = [8, 0,9,7,2,8,6,1,5]
    print(quick_sort(nums, 0, len(nums)-1))
    