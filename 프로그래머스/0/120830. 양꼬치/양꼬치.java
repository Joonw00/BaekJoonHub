class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        answer += n * 12000;
        int service = n / 10;
        k -= service;
        answer+= 2000*k;
        return answer;
    }
}