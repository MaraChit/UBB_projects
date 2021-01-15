using LAB_4.Extensions;
using LAB_4.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

namespace LAB_4.Implementation
{
    class EventDriven
    {
        private static List<string> PageLinks;

        public static void Run(List<string> hostnames)
        {
            PageLinks = hostnames;

            PageLinks.ForEach(link => {
                StartClient(link);
                Thread.Sleep(5000);
            });
        }

        private static void StartClient(string host)
        {
            var iPHostEntry = Dns.GetHostEntry(host.Split('/')[0]);
            var iPAddress = iPHostEntry.AddressList[0];

            var client = new Socket(iPAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);

            var state = new State
            {
                Socket = client,
                Hostname = host.Split('/')[0],
                Endpoint = host.Contains("/") ? host.Substring(host.IndexOf("/")) : "/",
                RemoteEndpoint = new IPEndPoint(iPAddress, 80),
            };

            state.Socket.BeginConnect(state.RemoteEndpoint, Connected, state);
        }

        #region Connect

        private static void Connected(IAsyncResult asyncResult)
        {
            var state = (State)asyncResult.AsyncState;

            state.Socket.EndConnect(asyncResult);
            Console.WriteLine($"Socket connected to {state.Hostname} ({state.Socket.RemoteEndPoint})\n");

            var byteData = Encoding.ASCII.GetBytes(state.GetRequestString());

            state.Socket.BeginSend(byteData, 0, byteData.Length, 0, Sent, state);
        }

        #endregion

        #region Send

        private static void Sent(IAsyncResult asyncResult)
        {
            var state = (State)asyncResult.AsyncState;

            var bytesSent = state.Socket.EndSend(asyncResult);
            Console.WriteLine($"Sent {bytesSent} bytes to server.\n");

            state.Socket.BeginReceive(state.Buffer, 0, state.Buffer.Length, 0, Recieved, state);
        }

        #endregion

        #region Recieve

        private static void Recieved(IAsyncResult asyncResult)
        {
            var state = (State)asyncResult.AsyncState;

            var bytesRead = state.Socket.EndReceive(asyncResult);

            state.ResponseContent += Encoding.ASCII.GetString(state.Buffer, 0, bytesRead);

            if (!state.IsFullResponse())
                state.Socket.BeginReceive(state.Buffer, 0, state.Buffer.Length, 0, Recieved, state);
                
            else if (state.ResponseBody.Length < state.ContentLength)   
                    state.Socket.BeginReceive(state.Buffer, 0, state.Buffer.Length, 0, Recieved, state);
                    
            else
            {
                Console.WriteLine($"Response received : expected {state.ContentLength} chars in body, got {state.ResponseContent.Length} chars (headers + body)\n");

                state.Socket.Shutdown(SocketShutdown.Both);
                state.Socket.Close();
            }
            
        }

        #endregion
    }
}
