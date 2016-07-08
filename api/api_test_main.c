/*
 * =====================================================================================
 *
 *       Filename:  api_test_main.c
 *
 *    Description:  Testing Case
 *
 *        Version:  1.0
 *        Created:  7/6/2016 5:45:28 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Zhi-wei YAN (Jerod YAN), jerod.yan@gmail.com
 *        Company:  DrumTm
 *
 * =====================================================================================
 */
#include "log_vgtp_pe.h"
#include <stdio.h>
int main(void)
{
    int ret = 0;
    ret = printf("Testing BEGIN.\n");

    int max_id = 9;
    char s_desc[] = "TEST_S";
    int data_len = 121;
    char data_val[] = "FID:00000 | REF_ID:-0001 | SC: NO | TYPE:I | UNC:0000 | MVM:0000 | PRE:0000 | VID:0000 | TXT:1645 | PIC:6515 | TIME:0070 ";

    for(int i=0; i<max_id; i++) {
        ret = log_vgtp_pe_sync(i, s_desc, data_len, data_val);
    }
    ret = printf("Testing   END.\n");

    return 1;
}
