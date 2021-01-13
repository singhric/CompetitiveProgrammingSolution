/**
 * Contest: July Cook-Off 2012
 * Problem: Ceil and Receipt (CIELRCPT)
 * Author: Maxim Kolosovskiy (Tester)
 */

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static void main(String[] args) throws IOException {
		new Main().run();
	}

	private void run() throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int cnt = Integer.parseInt(in.readLine());
		for (int tst = 1; tst <= cnt; tst++) {
			int h = Integer.parseInt(in.readLine());
			int res = 0;
			for (int i = 0; i <= 17; i++) {
				if ((h & (1 << i)) == 0)
					continue;
				if (i <= 11) {
					res++;
				} else {
					res += (1 << (i - 11));
				}
			}
			System.out.println(res);
		}
	}

}
