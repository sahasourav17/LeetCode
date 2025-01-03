func waysToSplitArray(nums []int) int {
    total_sum := 0
    for _, num := range(nums){
        total_sum += num
    }
    l_sum, cnt := 0, 0

    for i:= 0; i < len(nums)-1; i++ {
        l_sum += nums[i]
        r_sum := total_sum-l_sum

        if l_sum >= r_sum {
            cnt += 1
        }
    }

    return cnt
}
