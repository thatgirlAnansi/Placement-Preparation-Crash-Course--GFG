# There is a maze of size n°n. Tom is sitting at (0, 0). Jerry is sitting in another cell. There are k pieces of cheese placed in k different cells (k <= 10). Some cells are blocked while some are not. Tom can move to 4 cells at any time (left, right, up, down one position). Tom has to collect all the pieces of cheese and then reach Jerry's cell. You need to print the minimum no. of steps required to do so.

# The maze can be represented as an array of strings, where

# • if maze[i][j] is '#', then the cell is blocked,

# if maze[i][j] is '*", then the maze cell is not blocked,

# • if maze is '1', then the cell contains cheese(it is guaranteed that this cell is not blocked).

# if maze[] is 'D', then the cell is the destination cell where jerry is sitting(it is guaranteed that this cell is not blocked, and there is exactly one cell of this type)

# Note: Consider zero-based indexing.


# Note: Consider zero-based indexing.

# Input:

# maze = {"1",
# "*",
# "##D"}

# Output: 4

# Explanation:

# The optimal path will be (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2)

# Example 2:

# Input:

# maze = "1"".

# "*##".

# "#D*"]

# Output: -1

# Explanation: It is not possible to reach the jerry cell.
# Your Task:

# You don't need to read, input, or print anything. Your task is to complete the function solve( ), which takes an array of string maze[] as input parameters and returns the minimum possible answer to the problem.

# Constraints:

# 3≤n≤100

# maze [i][j]={ '1', 'D', '', '#}

# 1≤k≤10

# /{Driver Code Starts

# // Initial Template for C++

# #include <bits/stdc++.h>

# using namespace std;

# // Driver Code Ends

# //User function Template for C++

# -class Solution{

# public:

# int solve(vector<string> maze)

# {

# //Your code here

# }

# };

# // Driver Code Starts.

# int main()

# {

# int t;

# cin >> t;

# while(t--)

# {

# int n;

# cin >> n;

# vector<string> maze(n);

# for (int i = 0; i < n; i++)

# cin >> maze[1];

# Solution ob;

# cout << ob.solve(maze) << "\n";

# }

# return 0;

# // Driver Code Ends


include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Directions for movement: right, down, left, up
    vector<pair<int, int>> directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    // Function to check if a position is within bounds and not blocked
    bool isValid(int x, int y, vector<string>& maze) {
        return x >= 0 && y >= 0 && x < maze.size() && y < maze[0].size() && maze[x][y] != '#';
    }

    // BFS to find the shortest path from start to all reachable positions
    vector<vector<int>> bfs(int startX, int startY, vector<string>& maze) {
        int n = maze.size(), m = maze[0].size();
        vector<vector<int>> distance(n, vector<int>(m, INT_MAX));
        queue<pair<int, int>> q;
        q.push({startX, startY});
        distance[startX][startY] = 0;

        while (!q.empty()) {
            auto [x, y] = q.front();
            q.pop();

            for (auto [dx, dy] : directions) {
                int newX = x + dx, newY = y + dy;
                if (isValid(newX, newY, maze) && distance[newX][newY] == INT_MAX) {
                    distance[newX][newY] = distance[x][y] + 1;
                    q.push({newX, newY});
                }
            }
        }
        return distance;
    }

    int solve(vector<string> maze) {
        int n = maze.size();
        vector<pair<int, int>> cheesePositions;
        pair<int, int> tomPos = {0, 0}, jerryPos;

        // Locate positions of cheese and Jerry
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < maze[i].size(); j++) {
                if (maze[i][j] == 'D') {
                    jerryPos = {i, j};
                } else if (maze[i][j] == '1') {
                    cheesePositions.push_back({i, j});
                }
            }
        }

        int k = cheesePositions.size();
        vector<vector<int>> cheeseDistance(k + 1, vector<int>(k + 1, INT_MAX));

        // BFS from Tom's position
        auto tomDist = bfs(tomPos.first, tomPos.second, maze);
        
        // Check distances from Tom to each cheese
        for (int i = 0; i < k; i++) {
            auto cheeseDist = bfs(cheesePositions[i].first, cheesePositions[i].second, maze);
            cheeseDistance[0][i + 1] = tomDist[cheesePositions[i].first][cheesePositions[i].second];
            for (int j = 0; j < k; j++) {
                cheeseDistance[i + 1][j + 1] = cheeseDist[cheesePositions[j].first][cheesePositions[j].second];
            }
        }

        // BFS from last cheese to Jerry
        auto lastCheeseDist = bfs(jerryPos.first, jerryPos.second, maze);
        for (int i = 0; i < k; i++) {
            cheeseDistance[i + 1][k + 1] = lastCheeseDist[cheesePositions[i].first][cheesePositions[i].second];
        }

        // Calculate minimum distance using permutations
        int minSteps = INT_MAX;
        vector<int> cheeseOrder(k);
        iota(cheeseOrder.begin(), cheeseOrder.end(), 1); // Fill with {1, 2, ..., k}

        do {
            int totalDist = cheeseDistance[0][cheeseOrder[0]];
            for (int i = 0; i < k - 1; i++) {
                totalDist += cheeseDistance[cheeseOrder[i]][cheeseOrder[i + 1]];
            }
            totalDist += cheeseDistance[cheeseOrder[k - 1]][k + 1];
            minSteps = min(minSteps, totalDist);
        } while (next_permutation(cheeseOrder.begin(), cheeseOrder.end()));

        return minSteps == INT_MAX ? -1 : minSteps;
    }
};

// Driver Code
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<string> maze(n);
        for (int i = 0; i < n; i++)
            cin >> maze[i];

        Solution ob;
        cout << ob.solve(maze) << "\n";
    }
    return 0;
}
