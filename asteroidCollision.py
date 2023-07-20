class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0
        while i < len(asteroids)-1:
            if (asteroids[i] > 0 and asteroids[i+1] < 0):

                # suppose [8,-8]
                if abs(asteroids[i] == abs(asteroids[i+1])):
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i = max(0, i-1)
                else:
                    if abs(asteroids[i]) < abs(asteroids[i+1]):
                        asteroids.pop(i)
                    else:
                        asteroids.pop(i+1)
                    i = max(0, i-1)
            else:
                i += 1
        return asteroids
