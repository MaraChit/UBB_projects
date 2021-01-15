using LAB_4.Extensions;
using LAB_4.Model;
using System;
using System.Collections.Generic;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading.Tasks;

namespace LAB_4.Implementation
{
    class AsyncTaskDriven
    {
        private static List<string> PageLinks;

        public static void Run(List<string> hostnames)
        {
            PageLinks = hostnames;

            var tasks = new List<Task>();

            PageLinks.ForEach(link =>
            {
                tasks.Add(Task.Run(() => StartClient(link)));
            });

            Task.WaitAll(tasks.ToArray());
        }

        private static async void StartClient(string host)
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

            await ConnectWrapper(state);

            await SendWrapper(state, state.GetRequestString());

            await ReceiveWrapper(state);

            Console.WriteLine($"Response received : expected {state.ContentLength} chars in body, got {state.ResponseContent.Length} chars (headers + body)");

            client.Shutdown(SocketShutdown.Both);
            client.Close();
        }

        #region Connect

        private static async Task ConnectWrapper(State state)
        {
            state.Socket.BeginConnect(state.RemoteEndpoint, ConnectCallback, state);

            await Task.FromResult(state.IsConnected.WaitOne());
        }

        private static void ConnectCallback(IAsyncResult asyncResult)
        {
            var state = (State)asyncResult.AsyncState;

            state.Socket.EndConnect(asyncResult);

            Console.WriteLine($"Socket connected to {state.Hostname} ({state.Socket.RemoteEndPoint})");

            state.IsConnected.Set();
        }

        #endregion

        #region Send

        private static async Task SendWrapper(State state, string data)
        {
            var byteData = Encoding.ASCII.GetBytes(data);

            state.Socket.BeginSend(byteData, 0, byteData.Length, 0, SendCallback, state);

            await Task.FromResult(state.IsSend.WaitOne());
        }

        private static void SendCallback(IAsyncResult asyncResult)
        {
            var state = (State)asyncResult.AsyncState;

            var bytesSent = state.Socket.EndSend(asyncResult);
            Console.WriteLine($"Sent {bytesSent} bytes to server.");

            state.IsSend.Set();
        }
        #endregion

        #region Recieve

        private static async Task ReceiveWrapper(State state)
        {
            state.Socket.BeginReceive(state.Buffer, 0, state.Buffer.Length, 0, ReceiveCallback, state);

            await Task.FromResult(state.IsRecieved.WaitOne());
        }

        private static void ReceiveCallback(IAsyncResult asyncResult)
        {
            var state = (State)asyncResult.AsyncState;

            var bytesRead = state.Socket.EndReceive(asyncResult);

            state.ResponseContent += Encoding.ASCII.GetString(state.Buffer, 0, bytesRead);

            if (!state.IsFullResponse())
                state.Socket.BeginReceive(state.Buffer, 0, state.Buffer.Length, 0, ReceiveCallback, state);

            else if (state.ResponseBody.Length < state.ContentLength)
                state.Socket.BeginReceive(state.Buffer, 0, state.Buffer.Length, 0, ReceiveCallback, state);

            else
                state.IsRecieved.Set();


        }
        #endregion
    }
}
