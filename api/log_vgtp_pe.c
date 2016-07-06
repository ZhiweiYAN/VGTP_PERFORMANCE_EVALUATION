/*
 * =====================================================================================
 *
 *       Filename:  log_vgtp_pe.c
 *
 *    Description:  The API provided to logging the performance parameters
 *                  of VGTP (Vaxum Graphic/Image Transfer Protocol)
 *
 *        Version:  1.0
 *        Created:  7/6/2016 12:03:26 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Zhi-wei YAN (Jerod YAN), jerod.yan@gmail.com
 *        Company:  Vanxum
 *
 * =====================================================================================
 */

#include	"log_vgtp_pe.h"
/* 
 * ===  FUNCTION  ======================================================================
 *         Name:  int log_vgtp_pe_sync()
 *  Description:  logging VGTP performance parameters 
 * =====================================================================================
 */
int log_vgtp_pe_sync(int s_id, char *s_desc, int data_len, char* data_val)
{
    //Check the input parameters
    DBG("Check the input parameters.\n");
    if(0 > s_id){
        printf("Input parameters error: s_id = %d.\n", s_id);
        return -1;
    }

    if(NULL==s_desc){
        printf("Input parameters error: s_desc = NULL.\n");
        return -2;
    }
        
    if(0>=data_len || data_len >= REDIS_CMD_BUFFER_LEN){
        printf("Input parameters error: data_len = %d.\n", data_len);
        return -3;
    }

    if(NULL==data_val){
        printf("Input parameters error: data_val = NULL.\n");
        return -4;
    }

    if(data_len != (int)strlen(data_val) ){
        printf("Input parameters error: len(data_val) = %d and data_len = %d.\n", 
                strlen(data_val), data_len);
        return -5;
    }


    //Connect the Redis Database
    DBG("Prepare Redis DB:\n");
    redisContext *redis_con = NULL;
    redisReply *redis_reply = NULL;

    const char * redis_hostname = REDIS_SRV_IP;
    int redis_port = REDIS_SRV_PORT;
    struct timeval redis_timeout = {1, REDIS_TIMEOUT};

    redis_con = redisConnectWithTimeout(redis_hostname, redis_port, redis_timeout);
    if(NULL==redis_con || redis_con->err) {
        if(redis_con) {
            printf("Redis connection error: %s\n", redis_con->errstr);
            redisFree(redis_con);
            redis_con = NULL;
        } else {
            printf("Redis Connection error: can't allocate redis context.\n");
        }
        return -1;
    } else {
        DBG("Redis Connection Success.\n");
        redis_reply = (redisReply*)redisCommand(redis_con, "Ping");
        DBG("Ping: %s\n", redis_reply->str);
        freeReplyObject(redis_reply);
        redis_reply= NULL;
    }

    //Save the performance parameters into Redis DB.
    char cmd_buffer[REDIS_CMD_BUFFER_LEN];
    memset((void*)cmd_buffer, 0, REDIS_CMD_BUFFER_LEN);

    sprintf(cmd_buffer, "rpush %s \"ID:%d|DESC:%s|%s\"", REDIS_PE_STAT_LIST, s_id, s_desc, data_val);
    DBG("cmd_buffer: %s\n", cmd_buffer);
    redis_reply = (redisReply*)redisCommand(redis_con,cmd_buffer);

    if(NULL == redis_reply
           ||redis_reply->type == REDIS_REPLY_ERROR
           ||redis_reply->type == REDIS_REPLY_NIL) {
            printf("RedisDB reply is NULL or ErrCode = |%s|", redis_reply->str);
            return -1;
    }

    //free redis_reply objects
    if(NULL != redis_reply) {
        freeReplyObject(redis_reply);
        redis_reply = NULL;
    }    

    //free redis conn
    if(NULL != redis_con){
        redisFree(redis_con);
        redis_con = NULL;
    }

    return 1;
}

int log_vgtp_pe_async(int s_id, char *s_desc, int data_len, char* data_val)
{
    return 1;
}
