require "csv"
require "cgi"

PROJECT_ROOT = File.dirname(__FILE__)
DATA_DIR = "#{PROJECT_ROOT}/data"

def csv_table(filename)
  CSV.foreach("#{DATA_DIR}/#{filename}", :headers => true) do |row|
    yield Hash[row.map { |k,v| [k, CGI.escapeHTML(v.to_s)] }]
  end
end
