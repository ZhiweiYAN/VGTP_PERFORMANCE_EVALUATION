/*
 * =====================================================================================
 *
 *       Filename:  log_vgtp_pe.h
 *
 *    Description:  The API provided to logging the performance parameters
 *                  of VGTP (Vaxum Graphic/Image Transfer Protocol)
 *
 *        Version:  1.0
 *        Created:  7/6/2016 12:00:17 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Zhi-wei YAN (Jerod YAN), jerod.yan@gmail.com
 *        Company:  Vanxum
 *
 * =====================================================================================
 */

#ifndef  LOG_VGTP_PE_H_INC
#define  LOG_VGTP_PE_H_INC

#include <hiredis/hiredis.h>
#include <stdio.h>
#include <string.h>

#define REDIS_SRV_IP "127.0.0.1"
#define REDIS_SRV_PORT 6379
#define REDIS_TIMEOUT 500000
#define REDIS_CMD_BUFFER_LEN 8192
#define REDIS_PE_STAT_LIST "PE_STAT_LIST"

#define MAX_STRING_SIZE 16384

#ifdef DEBUG
#define DBG(format, args...) do{printf("LOG_VGTP_DBG INFO:"); printf(format, ##args);fflush(NULL);}while(0);
#else
#define DBG(format, args...)
#endif
int log_vgtp_pe_sync(int s_id, char *s_desc, int data_len, char* data_val);
int log_vgtp_pe_async(int s_id, char *s_desc, int data_len, char* data_val);


#endif   /* ----- #ifndef LOG_VGTP_PE_H_INC  ----- */
