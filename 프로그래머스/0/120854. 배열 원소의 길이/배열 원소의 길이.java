class Solution {
    public int[] solution(String[] strlist) {
        int l = strlist.length;
        int[] answer = new int[l];
        for(int i=0;i<l;i++){
            answer[i] = strlist[i].length();
        }
        return answer;
    }
}