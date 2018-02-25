/*
 * =====================================================================================
 *
 *       Filename:  writer.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  2011-12-08 12:03:21
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  jiye (search engine group), jiye@taobao.com
 *        Company:  www.taobao.com
 *
 * =====================================================================================
 */


#include    <stdlib.h>
#include    <iostream>
#include    <fstream>
#include    "lm.helloworld.pb.h"

using namespace std;

int main(void)
{

    lm::helloworld msg1;
    msg1.set_id(101);
    msg1.set_str("hellow");

    // Write the new address book back to disk.
    fstream output("./log", ios::out | ios::trunc | ios::binary);

    if (!msg1.SerializeToOstream(&output)) {
        cerr << "Failed to write msg." << endl;
        return -1;
    }
    return 0;
}