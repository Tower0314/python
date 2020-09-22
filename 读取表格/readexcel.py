#coding=gbk
import xlrd
import xlwt

def read_excel():

    workBook = xlrd.open_workbook('test.xls');

    # 1.��ȡsheet������
    # 1.1 ��ȡ����sheet������(list����)
    allSheetNames = workBook.sheet_names();
    print(allSheetNames);

    # 1.2 �������Ż�ȡsheet�����֣�string���ͣ�
    sheet1Name = workBook.sheet_names()[0];
    print(sheet1Name);

    # 2. ��ȡsheet����
    ## 2.1 ��1���������Ż�ȡsheet����
    sheet1_content1 = workBook.sheet_by_index(0); # sheet������0��ʼ
    ## 2.2 ��2����sheet���ֻ�ȡsheet����
    sheet1_content2 = workBook.sheet_by_name('Sheet1');

    # 3. sheet�����ƣ�����������
    print(sheet1_content1.name,sheet1_content1.nrows,sheet1_content1.ncols);

    # 4. ��ȡ���к����е�ֵ�����飩
    rows = sheet1_content1.row_values(3); # ��ȡ����������
    cols = sheet1_content1.col_values(2); # ��ȡ����������
    print(rows);

    # 5. ��ȡ��Ԫ������(���ַ�ʽ)
    print(sheet1_content1.cell(1, 0).value);
    print(sheet1_content1.cell_value(2, 2));
    print(sheet1_content1.row(2)[2].value);

    # 6. ��ȡ��Ԫ�����ݵ���������
    # Tips: python��ȡexcel�е�Ԫ������ݷ��ص���5������ [0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error]
    print(sheet1_content1.cell(1, 0).ctype);


if __name__ == '__main__':
    read_excel();