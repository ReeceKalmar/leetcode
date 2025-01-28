void merge(int *nums1, int nums1Size, int m, int *nums2, int nums2Size, int n) {
  int i, j = 0;

	while (i < m || j < n) {
		int n1 = nums1[i];
		int n2 = nums2[j];

		if (n2 < n1) {
			nums1[i + j] = n2;
			nums2[
		}
	}
}
