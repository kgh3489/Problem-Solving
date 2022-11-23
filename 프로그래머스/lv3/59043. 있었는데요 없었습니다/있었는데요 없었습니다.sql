SELECT A.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS B
ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME - B.DATETIME > 0
ORDER BY A.DATETIME