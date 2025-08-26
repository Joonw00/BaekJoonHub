import java.io.*;
import java.util.*;

public class Main {
    static class FastScanner {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer tokenizer;
        String next() throws IOException {
            while (tokenizer == null || !tokenizer.hasMoreElements()) {
                String line = reader.readLine();
                if (line == null) return null;
                tokenizer = new StringTokenizer(line);
            }
            return tokenizer.nextToken();
        }
        long nextLong() throws IOException { return Long.parseLong(next()); }
    }

    static long[] memoCountFree; 
    static long[] memoSumFree;  

    static long solveRange(long lower, long upper) {
        if (lower <= 0) return sumUpTo(upper);
        return sumUpTo(upper) - sumUpTo(lower - 1);
    }

    static long sumUpTo(long n) {
        if (n < 0) return 0;
        int[] digits = toDigits(n); 
        int totalPositions = digits.length;
        memoCountFree = new long[totalPositions + 1];
        memoSumFree   = new long[totalPositions + 1];
        Arrays.fill(memoCountFree, -1);
        Arrays.fill(memoSumFree, -1);
        long[] pair = dfs(0, 1, digits);
        return pair[1];
    }

    static long[] dfs(int positionIndex, int isTight, int[] digits) {
        int totalPositions = digits.length;
        if (positionIndex == totalPositions) {
            return new long[]{1, 0};
        }

        if (isTight == 0 && memoCountFree[positionIndex] != -1) {
            return new long[]{memoCountFree[positionIndex], memoSumFree[positionIndex]};
        }

        int limitDigit = (isTight == 1) ? digits[positionIndex] : 9;
        long totalCount = 0;
        long totalSum = 0;

        for (int chosenDigit = 0; chosenDigit <= limitDigit; chosenDigit++) {
            int nextTight = (isTight == 1 && chosenDigit == limitDigit) ? 1 : 0;
            long[] child = dfs(positionIndex + 1, nextTight, digits);
            long childCount = child[0];
            long childSum = child[1];
            totalCount += childCount;
            totalSum += childSum + (long) chosenDigit * childCount;
        }

        if (isTight == 0) {
            memoCountFree[positionIndex] = totalCount;
            memoSumFree[positionIndex] = totalSum;
        }
        return new long[]{totalCount, totalSum};
    }

    static int[] toDigits(long n) {
        String s = Long.toString(n);
        int[] arr = new int[s.length()];
        for (int i = 0; i < s.length(); i++) arr[i] = s.charAt(i) - '0';
        return arr;
    }

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();
        long lower = fs.nextLong();
        long upper = fs.nextLong();
        long result = solveRange(lower, upper);
        System.out.println(result);
    }
}
