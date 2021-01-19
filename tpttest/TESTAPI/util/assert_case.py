import json


class AssertCase:

    def message_assert_case(self, expect, result):
        """
        断言方法
        :param expect: 预期结果
        :param result: 实际结果
        :return:
        """
        if expect is not None:
            if json.dumps(expect) in json.dumps(result):
                print("----pass----")
                assert_data = True
            else:
                print("----fail----")
                assert_data = False
        else:
            assert_data = False
        return assert_data
        # for i in expect:
        #     if "." in i:
        #         expect_list = i.split(sep=".")
        #         if result[expect_list[0]][expect_list[1]][0][expect_list[2]] == expect[i]:
        #             print("----pass----")
        #         else:
        #             print("----fail----")
        #     else:
        #         if result[i] == expect[i]:
        #             print("----pass----")
        #         else:
        #             print("----fail----")

# if __name__ == '__main__':
#     result = {'code': '0000', 'msg': None, 'desc': None,
#               'data': {'currentPageIndex': 0, 'totalCount': 3, 'pageSize': 300, 'haveNextPage': True, 'totalPages': 1,
#                 'customerAllPolicyList': [{'policyCode': '000092406879922', 'statusName': '保障中', 'productName': '太平质安心质子重离子医疗保险', 'applicantId': 255699295, 'applicantName': '章豹', 'insuredId': 255699295, 'insuredName': '章豹', 'validateDate': '2020-04-28', 'pauseDate': '', 'endDate': '2056-04-27', 'policyType': 1, 'polInsuId': None, 'riskCode': None, 'licenseNo': None, 'polProductName': None}], 'isView': '0'}}
#     expect = {"data.customerAllPolicyList.policyCode": "000092406879922"}
#     expect1 = {"code": '0000'}
#     AssertCase().message_assert_case(expect, result)