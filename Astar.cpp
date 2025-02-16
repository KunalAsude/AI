#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

const int ROWS = 3, COLS = 3;

struct Node {
    int x, y, cost, heuristic, parentX, parentY;
    Node(int x, int y, int cost, int heuristic, int parentX, int parentY) {
        this->x = x;
        this->y = y;
        this->cost = cost;
        this->heuristic = heuristic;
        this->parentX = parentX;
        this->parentY = parentY;
    }
};

struct Compare {
    bool operator()(Node a, Node b) {
        return (a.cost + a.heuristic) > (b.cost + b.heuristic);
    }
};

int heuristic(int x1, int y1, int x2, int y2) {
    return abs(x1 - x2) + abs(y1 - y2);
}

void printPath(Node parent[ROWS][COLS], int sx, int sy, int gx, int gy) {
    int x = gx, y = gy;
    while (x != sx || y != sy) {
        cout << "(" << x << ", " << y << ") -> ";
        int tempX = parent[x][y].parentX;
        int tempY = parent[x][y].parentY;
        x = tempX;
        y = tempY;
    }
    cout << "(" << sx << ", " << sy << ") -> Goal\n";
}

void AStar(int grid[ROWS][COLS], int sx, int sy, int gx, int gy) {
    priority_queue<Node, deque<Node>, Compare> openSet;
    openSet.push(Node(sx, sy, 0, heuristic(sx, sy, gx, gy), -1, -1));

    int dx[] = {-1, 1, 0, 0}, dy[] = {0, 0, -1, 1};
    bool visited[ROWS][COLS] = {false};
    Node parent[ROWS][COLS] = {Node(-1, -1, 0, 0, -1, -1)};

    while (!openSet.empty()) {
        Node current = openSet.top();
        openSet.pop();

        if (current.x == gx && current.y == gy) {
            printPath(parent, sx, sy, gx, gy);
            return;
        }

        if (visited[current.x][current.y]) continue;
        visited[current.x][current.y] = true;

        for (int i = 0; i < 4; i++) {
            int nx = current.x + dx[i], ny = current.y + dy[i];
            if (nx >= 0 && nx < ROWS && ny >= 0 && ny < COLS && grid[nx][ny] == 0 && !visited[nx][ny]) {
                openSet.push(Node(nx, ny, current.cost + 1, heuristic(nx, ny, gx, gy), current.x, current.y));
                parent[nx][ny] = current;
            }
        }
    }
}

int main() {
    int grid[ROWS][COLS] = {
        {0, 1, 0},
        {0, 0, 0},
        {1, 0, 0}
    };

    AStar(grid, 0, 0, 2, 2);
    return 0;
}
