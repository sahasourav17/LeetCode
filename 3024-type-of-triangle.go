func triangleType(nums []int) string {
	if !canFormTriangle(nums) {
		return "none"
	}
	if isEquilateral(nums) {
		return "equilateral"
	}
	if isIsosceles(nums) {
		return "isosceles"
	}
	return "scalene"
}

func canFormTriangle(nums []int) bool {
	return nums[0]+nums[1] > nums[2] &&
		nums[0]+nums[2] > nums[1] &&
		nums[1]+nums[2] > nums[0]
}

func isEquilateral(nums []int) bool {
	return nums[0] == nums[1] && nums[1] == nums[2]
}

func isIsosceles(nums []int) bool {
	return nums[0] == nums[1] || nums[1] == nums[2] || nums[0] == nums[2]
}
