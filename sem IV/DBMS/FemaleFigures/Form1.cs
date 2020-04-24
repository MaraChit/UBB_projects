using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace FemaleFigures
{

    public partial class Form1 : Form
    {
        SqlConnection connection;
        SqlDataAdapter daFemale, daNationality;
        DataSet ds;
        SqlCommandBuilder cb;
        BindingSource bsFemale, bsNationality;

        public Form1()
        {
            InitializeComponent();
        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            daFemale.Update(ds, "Female");
        }

        private void buttonConnect_Click(object sender, EventArgs e)
        {
            connection = new SqlConnection(@"Data Source = LAPTOP-0NLQETPR\SQLEXPRESS;Initial Catalog=HistoricalFemales; Integrated Security = True");
            ds = new DataSet();
            daFemale = new SqlDataAdapter("select * from Female", connection);
            daNationality = new SqlDataAdapter("select * from Nationality", connection);
            cb = new SqlCommandBuilder(daFemale);

            daFemale.Fill(ds, "Female");
            daNationality.Fill(ds, "Nationality");

            DataRelation dr = new DataRelation("FK_Nationality_Female",ds.Tables["Nationality"].Columns["Nid"], ds.Tables["Female"].Columns["Nid"]);
            ds.Relations.Add(dr);
            bsFemale = new BindingSource();
            bsNationality = new BindingSource();
            bsNationality.DataSource = ds;
            bsNationality.DataMember = "Nationality";
            bsFemale.DataSource = bsNationality;
            bsFemale.DataMember = "FK_Nationality_Female";

            dataGridView2.DataSource = bsFemale;
            dataGridView1.DataSource = bsNationality;

        }

    }
}
