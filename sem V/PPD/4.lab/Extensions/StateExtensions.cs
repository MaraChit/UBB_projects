using LAB_4.Model;
using System;
using System.Collections.Generic;
using System.Text;

namespace LAB_4.Extensions
{
    public static class StateExtensions
    {
        public static string GetRequestString(this State state)
            => $"GET {state.Endpoint} HTTP/1.1\r\n" +
                   $"Host: {state.Hostname}\r\n" +
                   "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36\r\n" +
                   "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,#1#*;q=0.8\r\n" +
                   "Accept-Language: en-US,en;q=0.9,ro;q=0.8\r\n" +
                   "Accept-Encoding: gzip, deflate\r\n" +
                   "Connection: keep-alive\r\n" +
                   "Upgrade-Insecure-Requests: 1\r\n" +
                   "Pragma: no-cache\r\n" +
                   "Cache-Control: no-cache\r\n"+
                   "Content-Length: 0\r\n\r\n";

        public static bool IsFullResponse(this State state) => state.ResponseContent.Contains("\r\n\r\n");
    }
}
