SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID #회원 ID와 상품 ID가 같은 것을 그룹핑
HAVING COUNT(*) > 1 #중복이라면
ORDER BY USER_ID,PRODUCT_ID DESC