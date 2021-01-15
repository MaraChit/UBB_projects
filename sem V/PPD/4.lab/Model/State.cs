using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace LAB_4.Model
{
    public class State
    {
        public Socket Socket { get; set; }

        public byte[] Buffer { get; set; }

        public string ResponseContent { get; set; }

        public string Hostname { get; set; }

        public string Endpoint { get; set; }

        public IPEndPoint RemoteEndpoint { get; set; }

        public ManualResetEvent IsConnected { get; set; }

        public ManualResetEvent IsSend { get; set; }

        public ManualResetEvent IsRecieved { get; set; }

        public string ResponseBody {
            get {
                var splitResponse = ResponseContent.Split(new[] { "\r\n\r\n" }, StringSplitOptions.RemoveEmptyEntries);

                return splitResponse.Length > 1 ? splitResponse[1] : "";
            }
        }

        public int ContentLength { 
            get {
                var contentLength = 0;
                var responseLines = ResponseContent.Split('\r', '\n');

                responseLines.ToList().ForEach(line =>
                {
                    var headerDetails = line.Split(':').Select(token => token.Trim()).ToArray();

                    contentLength = headerDetails[0].CompareTo("Content-Length") == 0 ? int.Parse(headerDetails[1].Trim()) : contentLength;
                });

                return contentLength;
            } 
        }

        public State()
        {
            IsConnected = new ManualResetEvent(false);
            IsSend = new ManualResetEvent(false);
            IsRecieved = new ManualResetEvent(false);

            Buffer = new byte[512];

            ResponseContent = "";
        }
    }
}
